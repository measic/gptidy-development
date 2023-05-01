import openai
from samples import *
openai.api_key = "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"

def get_response(context, content, operation):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a refactoring tool for Jupyter Notebooks. Notebook context: " + context},
        {"role": "user", "content": "CODE: " + content},
        {"role": "user", "content": "OPERATION: " + operation},
    ]
    )
    return completion.choices[0].message

# Q: What's your profession? What's the project about? Any other details?
context = "im a data scientist. this project is about heart attack analysis and prediction. the main point is to predict if a person is vulnerable to a heart attack or not"
content = ["data = pd.read_csv('data.csv')\n", "data.columns = ['age', 'rate']\n", "a = data['age'].mean()\n", "b = data['rate'].max()\n"]
operation = samples[Operation.RenameVariable]["prompt"]("data, a, and b")

print(get_response(context, str(content), operation))