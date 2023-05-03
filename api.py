import openai
openai.api_key = "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"

# does not work
def few_shot():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Project description: 'analyzing rainfall'"},
            {"role": "user", "content": "Task: Rename the variable 'data' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
            {"role": "system", "content": "Code: 'rainfall_data = pd.read_csv('data.csv')\nrainfall_data.columns = ['sun', 'mm']\na = rainfall_data['sun'].mean()\nb = rainfall_data['mm'].max()'"},
            {"role": "user", "content": "Task: Rename the variable 'a' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
            {"role": "system", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\nmean_sunshine = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Task: Rename the variable 'b' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
            {"role": "system", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nmax_rainfall_mm = data['mm'].max()'"},
            {"role": "user", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['ecg', 'blood']\na = data['ecg'].mean()\nb = data['blood'].max()'"},
            {"role": "user", "content": "Project description: 'looking at heart rate data'"},
            {"role": "user", "content": "Task: Rename the variable 'b' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
        ]
    )
    return completion.choices[0].message

# does not work
def cot():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Project description: 'analyzing rainfall'"},
            {"role": "user", "content": "Task: Rename the variable 'data' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
            {"role": "system", "content": "Code: 'rainfall_data = pd.read_csv('data.csv')\nrainfall_data.columns = ['sun', 'mm']\na = rainfall_data['sun'].mean()\nb = rainfall_data['mm'].max()' Explanation: 'I only renamed 'data' as that was the only variable requested to be renamed.'"},
            {"role": "user", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['ecg', 'blood']\na = data['ecg'].mean()\nb = data['blood'].max()'"},
            {"role": "user", "content": "Project description: 'looking at heart rate data'"},
            {"role": "user", "content": "Task: Rename the variable 'b' to a more descriptive name that reflects \
             the purpose of the variable, based on the project description and variable usage."},
        ]
    )
    return completion.choices[0].message

# works well
def get_response():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": str.format("Task: Rename the variable '{}' to a more descriptive name that reflects its purpose, based on the project description and variable usage.", 'b')},
            {"role": "user", "content": "Code: 'data = pd.read_csv('data.csv')\ndata.columns = ['sun', 'mm']\na = data['sun'].mean()\nb = data['mm'].max()'"},
            {"role": "user", "content": "Project description: 'analyzing rainfall'"},
            {"role": "user", "content": "Your format: ('original name', 'new name')"},
        ]
    )
    return completion.choices[0].message

# works well
def get_response2():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": str.format("Task: Rename the variable '{}' to a more descriptive name that reflects its purpose, based on the project description and variable usage.", 'df')},
            {"role": "user", "content": "Code: '# Creating copy of dataframe\ndf_copy = df\n\n# Encoding categorical features\ndf_copy = pd.get_dummies(df_copy, columns = cat_features, drop_first = True)\n\ndf_copy.columns'"},
            {"role": "user", "content": "Project description: 'im a data scientist. this project is about heart attack analysis and prediction. the main point is to predict if a person is vulnerable to a heart attack or not'"},
            {"role": "user", "content": "Your format: ('original name', 'new name')"},
        ]
    )
    return completion.choices[0].message


print(get_response2())
