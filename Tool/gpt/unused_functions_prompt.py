# using PT3

from Tool.notebook_processing import Notebook


task1_prompt = "A function/method is unused if it is defined using 'def' but is not referenced after being defined. Identify unused functions/methods in the code delimited by triple backticks. Output this as a list of function names."

task1_ex1_input = """```python
c = 5

def calc():
    a = 5
    b = 4
    return a + b
```"""

task1_ex1_output = "['calc']"

task1_ex2_input = """```python
def multiply(a, b):
    return a * b

c = 5

def special():
    a = 5
    b = 4
    return multiply(a, b)
```"""

task1_ex2_output = "['special']"

task1_ex3_input = """```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_name(self, name):
        self.name = name
```"""

task1_ex3_output = "['update_name']"

task1_ex4_input = """```python
def seven():
    return 7
```"""

task1_ex4_output = """['seven']"""


def unused_functions_prompt_task1(notebook: Notebook, cell_id: int):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']
    messages = [
        {"role": "user", "content": task1_prompt},
        {"role": "user", "content": task1_ex1_input},
        {"role": "assistant", "content": task1_ex1_output},
        {"role": "user", "content": task1_ex2_input},
        {"role": "assistant", "content": task1_ex2_output},
        {"role": "user", "content": task1_ex3_input},
        {"role": "assistant", "content": task1_ex3_output},
        {"role": "user", "content": task1_ex4_input},
        {"role": "assistant", "content": task1_ex4_output},
        {"role": "user", "content": f"```python\n{cell_src}\n```"}
    ]

    return messages


task2_prompt = "Remove the functions specified from the code snippet enclosed by triple backticks. Do not add, modify, or remove anything else. Output the updated code with the specified functions removed."

task2_ex1_input = """Code:
```python
c = 5

def random_adder():
    a = 2
    b = 3
    return a + b + c
```

Functions to remove:
['random_adder']"""

task2_ex1_output = """```python
c = 5
```"""

task2_ex2_input = """Code:
```python
par_val = 23
def multiply(a, b):
    return a * b
new_val = 1
```

Functions to remove:
['multiply']"""

task2_ex2_output = """```python
par_val = 23
new_val = 1
```"""

task2_ex3_input = """Code:
```python
def estimate(earnings):
    return 0.1 * earnings
```

Functions to remove:
['earnings']"""

task2_ex3_output = """```python
```"""

task2_ex4_input = """Code:
```python
def seven():
    return 7

def validate(val1, val2):
    assert val1 and val2
    val3 = seven()
    return val1 * val2 - val3
```

Functions to remove:
['seven', 'validate']"""

task2_ex4_output = """```python
```"""


def unused_functions_prompt_task2(notebook: Notebook, cell_id: int, function_names: list):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']
    messages = [
        {"role": "user", "content": task2_prompt},
        {"role": "user", "content": task2_ex1_input},
        {"role": "assistant", "content": task2_ex1_output},
        {"role": "user", "content": task2_ex2_input},
        {"role": "assistant", "content": task2_ex2_output},
        {"role": "user", "content": task2_ex3_input},
        {"role": "assistant", "content": task2_ex3_output},
        {"role": "user", "content": task2_ex4_input},
        {"role": "assistant", "content": task2_ex4_output},
        {"role": "user", "content": f"Code:\n```python\n{cell_src}\n```\n\nFunctions to remove:\n{function_names}"}
    ]

    return messages