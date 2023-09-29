# using PT2

task = "A variable is unused if it is assigned using an equals operator but is not referenced after being defined. Identify and remove unused variables in the code delimited by triple backticks. For unused variables in unpacking, change these to underscores. Ignore unused functions, imports, or classes. Output under the headings 'Unused variables' and 'Updated code'"

ex1_input = """```python
time = 5
d = 5
print(d)

def calc():
    a = 5
    b = 4
return a + b
```"""

ex1_output = """Unused variables:
['time']

Updated code:
```python
d = 5
print(d)

def calc():
    a = 5
    b = 4
    return a + b
```"""

ex2_input = """```python
val1 = 'hello'
val2 = 'world'
```"""

ex2_output = """Unused variables:
['val1', 'val2']

Updated code:
```python
```"""

ex3_input = """```python
z = [1, 2, 3]
a, b, c = z
print(a + b)
```"""

ex3_output = """Unused variables:
['c']

Updated code:
```python
z = [1, 2, 3]
a, b, _ = z
print(a + b)
```"""

ex4_input = """"```python
def associate():
    return center.path()

path = associate()
```"""

ex4_output = """Unused variables:
['path']

Updated code:
```python
def associate():
    return center.path()
```"""


def unused_variables_prompt(notebook: Notebook, cell_id: int):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']
    messages = [
        {"role": "user", "content": task},
        {"role": "user", "content": ex1_input},
        {"role": "assistant", "content": ex1_output},
        {"role": "user", "content": ex2_input},
        {"role": "assistant", "content": ex2_output},
        {"role": "user", "content": ex3_input},
        {"role": "assistant", "content": ex3_output},
        {"role": "user", "content": ex4_input},
        {"role": "assistant", "content": ex4_output},
        {"role": "user", "content": f"```python\n{cell_src}\n```"}
    ]
    return messages