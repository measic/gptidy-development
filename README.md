# gptidy-development

This is the main repository of my thesis, "Code Refactoring using Large Language Models in Jupyter Notebooks". In this repository, you will find all code related to the development of the gptidy tool, the evaluation of the tool, and the user study. You can recreate my entire selection, sampling, and evaluation process by running the associated notebooks.

The `gptidy` tool provides five code-related and three markdown-related refactoring operations tailored for Jupyter Notebooks. In particular, the tool considers the purpose of a notebook to tailor the refactoring operations to a specific notebook.

All code was written by me, excepted for the `tree_of_thought.py` file in the `evaluation` folder, which was adapted from [this repository](https://github.com/princeton-nlp/tree-of-thought-llm).

The repository contains the following folders:
- `tool`: contains the source code of the gptidy tool.
- `evaluation`: contains the evaluation notebooks and the analysis of the evaluation.
- `user study`: contains the user study notebooks and the analysis of the user study.

## `tool` folder
The tool folder contains the source code of the gptidy tool. We use the best performing prompting technique found during our evaluation in our research paper for each refactoring operation.

### Usage
First, make sure you have set up the OpenAI API key as an environment variable. Then, run:

`python3 gptidy.py <path to notebook>`

and follow the prompts provided.

## `evaluation` folder
The evaluation folder contains the notebooks used to evaluate the gptidy tool (automated). The `evaluation dataset` folder contains the dataset used for the evaluation and code used to download and process the dataset, adapted from [this repository]()

. Also included are the `notebooks` and `all_cells` folders which contain the collection of 233 notebooks and 6,095 code cells. The remaining folders are specific to each refactoring operation and contain the notebooks used for the evaluation and the analysis of the evaluation using GPT.

You can recreate all evaluations by running the notebooks in each refactoring operation/prompting technique combination folder. Each refactoring operation contains a folder for P1 - P4 (each of the four prompting techniques used) and its associated notebook. Also included is the code for determining the cells used for each refactoring operation and the code for the sampling process.

## `user study` folder
This folder contains the creation of the dataset and analysis of the results for the user study conducted on Google Forms. The `study1` folder contains the code used to determine the samples used in evaluating GPT's variable/function names. The `study2` folder contains the code used to generate the introduction, code explanation, and conclusion cell for the Titanic notebook from Kaggle. The House notebook from Kaggle is also included but we did not end up using this in our user study. Finally, the `results` folder contains the analysis of the results from the user study entirely.