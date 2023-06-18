import openai
openai.api_key = "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"
import testing
# works well


def rename_variable_example():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": str.format(
                "Task: Rename the variable '{}' to a more descriptive name that reflects its purpose, based on the project description and variable usage.", 'b')},
            {"role": "user",
                "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Project description: 'analyzing rainfall'"},
            {"role": "user",
                "content": "Your format: ('original name', 'new name')"},
        ]
    )
    return completion.choices[0].message

# works well


def rename_variable_example2():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": str.format(
                "Task: Rename the variable '{}' to a more descriptive name that reflects its purpose, based on the project description and variable usage.", 'df')},
            {"role": "user",
                "content": "Code: '# Creating copy of dataframe\ndf_copy = df\n\n# Encoding categorical features\ndf_copy = pd.get_dummies(df_copy, columns = cat_features, drop_first = True)\n\ndf_copy.columns'"},
            {"role": "user", "content": "Project description: 'im a data scientist. this project is about heart attack analysis and prediction. the main point is to predict if a person is vulnerable to a heart attack or not'"},
            {"role": "user",
                "content": "Your format: ('original name', 'new name')"},
        ]
    )
    return completion.choices[0].message


def prompt():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=0,
        messages= testing.rename_function
    )
    return completion.choices[0].message

print(prompt()["content"])