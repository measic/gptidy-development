import openai
from prompts import *
openai.api_key = "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"


def get_response():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": "Task: Rename the variable below to a more descriptive name that reflects \
         the purpose of the variable, based on the project description and variable usage."},
            {"role": "user",
             "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Variable: 'data'"},
            {"role": "user", "content": "Project description: 'analyzing rainfall'"},
            {"role": "user", "content": "Output the variable name and a one sentence explanation"},
        ]
    )
    return completion.choices[0].message


print(get_response())
