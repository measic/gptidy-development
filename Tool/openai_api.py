import openai
import re
my_key = "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"
han = "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"
openai.api_key = my_key

def prompt_cot(n, stop, input_code, input_msg):
    msgs = [
            {"role": "user", "content": "A function/method is unused if it is defined using `def` but is not referenced after being defined. Remove unused functions/methods in the code delimited by triple backticks. First, identify unused functions in the code. Then, remove the identified unused functions from the code. Output under the headings 'Unused functions' and 'Updated code' respectively."},
            {"role": "user", "content": "```python\nc = 5\n\ndef calc():\n    a = 5\n    b = 4\n    return a + b```"},
            {"role": "assistant", "content": "Unused functions:\n['calc']\n\nUpdated code:\n```python\nc = 5```\n\nExplanation:\nFully removed the functions ['calc'] and the code inside these functions."},
            {"role": "user", "content": "```python\ndef multiply(a, b):\n    return a * b\n\ndef mystery():\n    a = 5\n    b = 4\n    return a - b```"},
            {"role": "assistant", "content": "Unused functions:\n['multiply', 'mystery']\n\nUpdated code:\n```python\n```\n\nExplanation:\nFully removed the functions ['mystery', 'multiply'] and the code inside these functions"},
            {"role" : "user", "content" : f"```{input_code}```"},   
        ]
    if input_msg:
        msgs.append({"role" : "assistant", "content" : input_msg})
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages= msgs,
        n = n,
        stop = stop,
    )
    return completions

def prompt_vote(n, stop, original_code, unused_functions, choice1, choice2):
    msgs = [
            {"role": "user", "content": "Given original code, a list of unused function names, and two updated code choices, decide which choice best removes the identified unused functions from the original code. Analyze each choice in detail, then conclude in the last line 'The best choice is {s}', where s is the integer id of the choice."},
            {"role": "user", "content": f"Original code:\n```python\nc = 5\n\ndef calc():\n    a = 5\n    b = 4\n    return a + b```\nUnused functions:\n['calc']\nChoice 1:\n```python\nc = 5\n\na = 5\n    b = 4```\nChoice 2:\n```python\nc = 5```"},
            {"role": "assistant", "content": "Choice 1 does not properly remove the unused functions ['calc']. While it does remove the function signature and return statement, it does not fully remove the contents of the function.\n\nChoice 2 properly removes the unused functions ['calc']. The functions identified are indeed unused and have been fully removed from the code.\n\nThe best choice is 2."},
            {"role": "user", "content": f"Original code:\n```python\n{original_code}```\nUnused functions:\n{unused_functions}\nChoice 1:\n```python\n{choice1}```\nChoice 2:\n```python\n{choice2}```"}
            ]
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages= msgs,
        n = n,
        stop = stop,
    )
    return completions

def solve(input_code):
    identify_trials = 5
    remove_trials = 2
    remove_vote_trials = 5

    # Identify unused items
    identify_stop = "Updated code:"
    identify_completions = prompt_cot(n = identify_trials, stop = identify_stop, input_code = input_code, input_msg = None)

    # Get identified items
    identified_names = []
    for i in range(identify_trials):
        lst = eval(identify_completions.choices[i]['message']['content'].split('Unused functions:')[1].strip("\n"))
        if type(lst) == list:
            lst.sort()
        identified_names.append(lst)
    
    # Convert to a list of strings so it is hashable
    identified_names = [str(item) for item in identified_names]
    
    # Vote on the most popular choice by counting the number of times each item appears
    # in the list of identified items (don't need ChatGPT for this)
    vote = {}
    for item in identified_names:
        if item in vote:
            vote[item] += 1
        else:
            vote[item] = 1
    
    # Get the most popular choice
    most_popular_identify = eval(max(vote, key=vote.get))

    # Remove the most popular choice from the code
    input_msg = f"Unused functions:\n{most_popular_identify}\n\n"
    remove_completions = prompt_cot(n = remove_trials, stop = None, input_code = input_code, input_msg = input_msg)

    # Get the updated code
    updated_code = []
    for i in range(remove_trials):
        code = remove_completions.choices[i]['message']['content'].split('```')[1].split('```')[0]
        if code.startswith('python'):
            code = code[6:]
        code = code.strip("\n")
        updated_code.append(code)

    # Vote on the best choice using GPT
    gpt_votes = prompt_vote(n = remove_vote_trials, stop = None, original_code = input_code, unused_functions = most_popular_identify, choice1 = updated_code[0], choice2 = updated_code[1])
    vote_results = [0] * remove_trials
    for i in range(remove_vote_trials):
        vote_output = gpt_votes.choices[i]['message']['content']
        pattern = r".*best choice is .*(\d+).*"
        match = re.match(pattern, vote_output, re.DOTALL)
        if match:
            vote = int(match.groups()[0]) - 1
            if vote in range(remove_trials):
                vote_results[vote] += 1
        else:
            print(f'vote no match: {[vote_output]}')
    
    # Get the most popular choice
    most_popular_remove = vote_results.index(max(vote_results))
    
    return most_popular_identify, updated_code[most_popular_remove]

test = "python\ndef clean_data (df, inplace = False):    column_filter = ['ISIN', 'Mnemonic', 'SecurityDesc', 'SecurityType', 'Currency', 'SecurityID', 'Date', 'Time', 'StartPrice', 'MaxPrice', 'MinPrice', 'EndPrice', 'TradedVolume', 'NumberOfTrades']    n_df = df[column_filter]    if not inplace:        n_df = df.copy ()            n_df.drop (n_df.Time == 'Time', inplace = True)    # we want the dates to be comparable to datetime.strptime()    n_df[\"CalcTime\"] = pd.to_datetime(\"1900-01-01 \" + n_df[\"Time\"], errors='coerce')    n_df[\"CalcDateTime\"] = pd.to_datetime(n_df[\"Date\"] + \" \" + n_df[\"Time\"], errors='coerce')    # Filter common stock    # Filter between trading hours 08:00 and 20:00    # Exclude auctions (those are with TradeVolume == 0)    only_common_stock = n_df[n_df.SecurityType == 'Common stock']    time_fmt = \"%H:%M\"    opening_hours_str = \"08:00\"    closing_hours_str = \"20:00\"    opening_hours = datetime.strptime(opening_hours_str, time_fmt)    closing_hours = datetime.strptime(closing_hours_str, time_fmt)    cleaned_common_stock = only_common_stock[(only_common_stock.TradedVolume > 0) & \                      (only_common_stock.CalcTime >= opening_hours) & \                      (only_common_stock.CalcTime <= closing_hours)]        bymnemonic = cleaned_common_stock[['Mnemonic', 'TradedVolume']].groupby(['Mnemonic']).sum()    number_of_stocks = 100    top = bymnemonic.sort_values(['TradedVolume'], ascending=[0]).head(number_of_stocks)    top_k_stocks = list(top.index.values)    cleaned_common_stock = cleaned_common_stock[cleaned_common_stock.Mnemonic.isin(top_k_stocks)]    sorted_by_index = cleaned_common_stock.set_index(['Mnemonic', 'CalcDateTime']).sort_index()    non_empty_days = sorted(list(cleaned_common_stock['Date'].unique()))    new_datetime_index = build_index(non_empty_days, opening_hours_str, closing_hours_str)[\"OrganizedDateTime\"].values        stocks = []    for stock in top_k_stocks:        stock = basic_stock_features(sorted_by_index, stock, new_datetime_index, inplace=True)        stocks.append(stock)    # prepared should contain the numeric features for all top k stocks,    # for all days in the interval, for which there were trades (that means excluding weekends and holidays)    # for all minutes from 08:00 until 20:00    # in minutes without trades the prices from the last available minute are carried forward    # trades are filled with zero for such minutes    # a new column called HasTrade is introduced to denote the presence of trades    prepared = pd.concat(stocks, axis=0).dropna(how='any')    prepared.Mnemonic = prepared.Mnemonic.astype('category')    return prepared"

res = solve(test)
print(res)