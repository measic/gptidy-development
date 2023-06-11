import openai
openai.api_key = "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"

# works well
def rename_variable_example():
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
def rename_variable_example2():
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

def extract_variable():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": "You will be given a code snippet, full code, and a project description. Your task is to perform the refactoring operation of variable extraction. Find the code snippet in the full code (must be exact) and extract it as a variable. Use the project description to come up with a meaningful variable name. Return the full modified code as output."},
            {"role": "user", "content": "Code snippet: `has_arg(tf.Session.run, key, True)`"},
            {"role": "user", "content": "Full code: " + g},
            {"role": "user", "content": "Project description: 'The purpose of the project is to develop the Keras library, which is a high-level deep learning API written in Python, designed to simplify and accelerate the development of machine learning applications, particularly with the TensorFlow platform, by providing a user-friendly interface and powerful functionalities.'"},
        ]
    )
    return completion.choices[0].message


print()
