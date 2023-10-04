# using PT3

from notebook_processing import Notebook


t1task = "Suggest a better name for the function specified in the code delimited by triple backticks that is more meaningful and better reflects its usage and/or better aligns with the project's purpose. Only suggest for the single function specified. Structure your response under the following headings: 'New function name' (only one function name) and 'Explanation' (a 1-2 sentence explanation of the new function name)."

t1ex1_input = """Project purpose:
This project is about analyzing top movie genre trends from 2000 to 2010. We will look at the top genres and top movies for each year.

Function to rename:
'dat'

Code:
```python
import pandas as pd

def dat(file_name):
    data = pd.read_csv(file_name)
    return data.head()

dat('data.csv')
```"""

t1ex1_output = """New function name:
'get_movie_data_df'

Explanation:
The new function name 'get_movie_data_df' reflects its usage to get a dataframe containing movie data."""

t1ex2_input = """Project purpose:
The focus of this project is determining the most common crime types in LA.

Function to rename:
'group'

Code:
```python
groups = df.groupby('gender')

def group(groups):
    for gender, grouped_data in groups:
        print(f"Gender: {gender}")
        print(grouped_data['crime_type'].value_counts())
        print("\n")
```"""

t1ex2_output = """New function name:
'print_group_crime_by_gender'

Explanation:
The new function name 'print_group_crime_by_gender' aligns with its purpose of printing the crime data grouped by gender."""

t1ex3_input = """Project purpose:
This repository contains a collection of graph theory assignments for MAT381.

Function to rename:
'visit'

Code:
```python
def visit(graph, vertex):
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')
    visit(graph, vertex)
```"""

t1ex3_output = """New function name:
'visit_vertex'

Explanation:
By renaming 'visit' to 'visit_vertex', it is now clearer that the function is being used to visit vertices."""

t1ex4_input = """Project purpose:
This project is for analyzing the relationship between the number of hours studied and the exam scores of students.

Function to rename:
'get'

Code:
```python
def get(x, y):
    return x.corr(y)

result, info = get(queue['Hours'], queue['Scores'])
print(result)
```"""

t1ex4_output = """New function name:
'calc_hours_scores_correlation'

Explanation:
The function name 'calc_hours_scores_correlation' reflects the purpose of the function, which is to calculate the correlation between the number of hours studied and the exam scores of students."""


def rename_function_prompt_task1(notebook: Notebook, cell_id: int, name: str):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']
    messages = [
        {"role": "user", "content": t1task},
        {"role": "user", "content": t1ex1_input},
        {"role": "assistant", "content": t1ex1_output},
        {"role": "user", "content": t1ex2_input},
        {"role": "assistant", "content": t1ex2_output},
        {"role": "user", "content": t1ex3_input},
        {"role": "assistant", "content": t1ex3_output},
        {"role": "user", "content": t1ex4_input},
        {"role": "assistant", "content": t1ex4_output},
        {"role": "user", "content": f"Project purpose:\n{notebook.purpose}\n\nFunction to rename:\n'{name}'\n\nCode:\n```python\n{cell_src}\n```"}
    ]

    return messages


t2ex1_input = """Rename the function 'dat' to 'get_movie_data_df' in the code delimited by triple backticks. Output the full code with the function renamed. Do not change anything else.
```python
import pandas as pd

def dat(file_name):
    data = pd.read_csv(file_name)
    return data.head()

dat('data.csv')
```"""

t2ex1_output = """```python
import pandas as pd

def get_movie_data_df(file_name):
    data = pd.read_csv(file_name)
    return data.head()

get_movie_data_df('data.csv')
```"""

t2ex2_input = """Rename the function 'group' to 'print_group_crime_by_gender' in the code delimited by triple backticks. Output the full code with the function renamed. Do not change anything else.
```python
groups = df.groupby('gender')

def group(groups):
    for gender, grouped_data in groups:
        print(f"Gender: {gender}")
        print(grouped_data['crime_type'].value_counts())
        print("\n")
```"""

t2ex2_output = """```python
groups = df.groupby('gender')

def print_group_crime_by_gender(groups):
    for gender, grouped_data in groups:
        print(f"Gender: {gender}")
        print(grouped_data['crime_type'].value_counts())
        print("\n")
```"""

t2ex3_input = """Rename the function 'visit' to 'visit_vertex' in the code delimited by triple backticks. Output the full code with the function renamed. Do not change anything else.
```python
def visit(graph, vertex):
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')
    visit(graph, vertex)
```"""

t2ex3_output = """```python
def visit_vertex(graph, vertex):
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')
    visit_vertex(graph, vertex)
```"""

t2ex4_input = """Rename the function 'get' to 'calc_hours_scores_correlation' in the code delimited by triple backticks. Output the full code with the function renamed. Do not change anything else.
```python
def get(x, y):
    return x.corr(y)

result, info = get(queue['Hours'], queue['Scores'])
print(result)
```"""

t2ex4_output = """```python
def calc_hours_scores_correlation(x, y):
    return x.corr(y)

result, info = calc_hours_scores_correlation(queue['Hours'], queue['Scores'])
print(result)
```"""


def rename_function_prompt_task2(notebook: Notebook, cell_id: int, before: str, after: str):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']

    messages = [
        {"role": "user", "content": t2ex1_input},
        {"role": "assistant", "content": t2ex1_output},
        {"role": "user", "content": t2ex2_input},
        {"role": "assistant", "content": t2ex2_output},
        {"role": "user", "content": t2ex3_input},
        {"role": "assistant", "content": t2ex3_output},
        {"role": "user", "content": t2ex4_input},
        {"role": "assistant", "content": t2ex4_output},
        {"role": "user", "content": f"Rename the function '{before}' to '{after}' in the code delimited by triple backticks. Output the full code with the function renamed. Do not change anything else.\n```python\n{cell_src}\n```"}
    ]

    return messages
