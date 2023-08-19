# token counter
import tiktoken


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def gpt_35_turbo_token_dollar_cost(input_str, output_str) -> int:
    # $0.0015 / 1000 tokens for input
    # $0.002 / 1000 tokens for output

    # get number of tokens
    input_tokens = num_tokens_from_string(input_str)
    output_tokens = num_tokens_from_string(output_str)

    # input cost
    input_cost = 0.0015 * input_tokens / 1000
    output_cost = 0.002 * output_tokens / 1000

    return input_cost + output_cost


def print_check_gpt_results(gpt_results):
    # checking finish reason for identified functions
    # check the 'reason' for each file in gpt_results and count them
    finish_reasons = {}
    for result in gpt_results:
        reason = result['reason']
        if reason in finish_reasons:
            finish_reasons[reason] += 1
        else:
            finish_reasons[reason] = 1

    # print the counts
    for reason, count in finish_reasons.items():
        print(f'{reason}: {count}')

    # determine which numbers did not finish
    finish_reason_failed = []
    for i, result in enumerate(gpt_results):
        reason = result['reason']
        if reason != 'stop':
            finish_reason_failed.append(i)

    # print the numbers
    return finish_reason_failed
    
def stats_results_unused(gpt_unused_names, before):
    # Identification results of Vulture vs GPT
    gpt_before_count = sum([len(lst) if lst is not None else 0 for lst in gpt_unused_names])
    vulture_before_count = sum([len(lst) for lst in before])
    print(f'GPT before count: {gpt_before_count}')
    print(f'Vulture before count: {vulture_before_count}')

    print("------------")

    # determine number of false and true positive identifications using gpt_unused_function_names and before
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    for i, gpt_names in enumerate(gpt_unused_names):
        before_names = before[i]
        gpt_names = gpt_names if gpt_names is not None else []
        for name in gpt_names:
            if name in before_names:
                true_positives += 1
            else:
                false_positives += 1

    for i, before_names in enumerate(before):
        gpt_names = gpt_unused_names[i] if gpt_unused_names[i] is not None else []
        for name in before_names:
            if name not in gpt_names:
                false_negatives += 1

    # print the results
    print(f'True positives: {true_positives}')
    print(f'False positives: {false_positives}')
    print(f'False negatives: {false_negatives}')