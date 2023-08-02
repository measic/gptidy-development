# token counter
import tiktoken


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens


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

    # determine which numbers did not finish due to length
    finish_reason_length = []
    for i, result in enumerate(gpt_results):
        reason = result['reason']
        if reason == 'length':
            finish_reason_length.append(i)

    # print the numbers
    print(finish_reason_length)
    