import openai
from prompts import *
openai.api_key = "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"

def get_response():
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
        {"role": "user", "content": "Suggest a new variable name for variables ['a, b, data'] \
         CONTEXT: {im analyzing rainfall data} \
         CODE: {data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()} \
         Output format: [list of tuples of variables and their new names]"},
    ]
    )
    return completion.choices[0].message

print(get_response())