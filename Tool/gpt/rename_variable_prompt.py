# using PT3

from Tool.notebook_processing import Notebook

t1task = "Suggest a better name for the variable specified in the code delimited by triple backticks that is more meaningful and better reflects its usage and/or better aligns with the project's purpose. Only suggest for the single variable specified. Structure your response under the following headings: 'New variable name' (only one variable name) and 'Explanation' (a 1-2 sentence explanation of the new variable name)."

t1ex1_input = """Project purpose:
This project is about analyzing top movie genre trends from 2000 to 2010. We will look at the top genres and top movies for each year.

Variable:
'dat'

Code:
```python
import pandas as pd

dat = pd.read_csv('data.csv')
dat.head()
```"""

t1ex1_output = """New variable name:
'movie_data_df'

Explanation:
The new variable name 'movie_data_df' reflects its usage as a dataframe containing movie data."""

t1ex2_input = """Project purpose:
The focus of this project is determining the most common crime types in LA.

Variable to rename:
'group'

Code:
```python
group = df.groupby('gender')

for gender, grouped_data in group:
    print(f"Gender: {gender}")
    print(grouped_data['crime_type'].value_counts())
    print("\n")
```"""

t1ex2_output = """New variable name:
'gender_crime_groups'

Explanation:
The new variable name 'gender_crime_groups' aligns with its purpose of grouping crime data by gender."""

t1ex3_input = """Project purpose:
This repository contains a collection of graph theory assignments for MAT381.

Variable to rename:
'queue'

Code:
```python
queue[0] = queue[0].lower()
while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
```"""

t1ex3_output = """New variable name:
'vertex_queue'

Explanation:
By renaming 'queue' to 'vertex_queue', it's now clearer that the variable is being used to store vertices."""

t1ex4_input = """Project purpose:
This project is for analyzing the relationship between the number of hours studied and the exam scores of students.

Variable to rename:
'result'

Code:
```python
result, info = pearsonr(queue['Hours'], queue['Scores'])
print(result)
```"""

t1ex4_output = """New variable name:
'hours_scores_correlation'

Explanation:
The variable name 'hours_scores_correlation' reflects the purpose of the variable, which is to store the correlation between the number of hours studied and the exam scores of students."""


def rename_variable_prompt_task1(notebook: Notebook, cell_id: int, name: str):
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
        {"role": "user", "content": f"Project purpose:\n{notebook.purpose}\n\nVariable to rename:\n'{name}'\n\nCode:\n```python\n{cell_src}\n```"}
    ]

    return messages


t2ex1_input = """Rename the variable 'dat' to 'movie_data_df' in the code delimited by triple backticks. Output the full code with the variable renamed. Do not change anything else.
```python
import pandas as pd

dat = pd.read_csv('data.csv')
dat.head()
```"""

t2ex1_output = """```python
import pandas as pd

movie_data_df = pd.read_csv('data.csv')
movie_data_df.head()
```"""

t2ex2_input = """Rename the variable 'group' to 'gender_crime_groups' in the code delimited by triple backticks. Output the full code with the variable renamed. Do not change anything else.
```python
group = df.groupby('gender')

for gender, grouped_data in group:
    print(f"Gender: {gender}")
    print(grouped_data['crime_type'].value_counts())
    print("\n")
```"""

t2ex2_output = """```python
gender_crime_groups = df.groupby('gender')

for gender, grouped_data in gender_crime_groups:
    print(f"Gender: {gender}")
    print(grouped_data['crime_type'].value_counts())
    print("\n")
```"""

t2ex3_input = """Rename the variable 'queue' to 'vertex_queue' in the code delimited by triple backticks. Output the full code with the variable renamed. Do not change anything else.
```python
queue[0] = queue[0].lower()
while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
```"""

t2ex3_output = """```python
vertex_queue[0] = vertex_queue[0].lower()
while vertex_queue:
    vertex = vertex_queue.popleft()
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            vertex_queue.append(neighbor)
            visited.add(neighbor)
```"""

t2ex4_input = """Rename the variable 'result' to 'hours_scores_correlation' in the code delimited by triple backticks. Output the full code with the variable renamed. Do not change anything else.
```python
result, info = pearsonr(queue['Hours'], queue['Scores'])
print(result)
```"""

t2ex4_output = """```python
hours_scores_correlation, info = pearsonr(queue['Hours'], queue['Scores'])
print(hours_scores_correlation)
```"""


def rename_variable_prompt_task2(notebook: Notebook, cell_id: int, before: str, after: str):
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
        {"role": "user", "content": f"Rename the variable '{before}' to '{after}' in the code delimited by triple backticks. Output the full code with the variable renamed. Do not change anything else.\n```python\n{cell_src}\n```"}
    ]

    return messages
