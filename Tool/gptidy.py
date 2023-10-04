import sys
import json
from Tool.gpt.rename_function_prompt import rename_function_prompt_task1, rename_function_prompt_task2
from notebook_processing import Notebook
from gpt.gpt import gpt_wrapper, gpt_unpack_simple
from Tool.gpt.markdown_prompts import introduction_prompt, summarize_cell_prompt, conclusion_prompt
from Tool.gpt.unused_variables_prompt import unused_variables_prompt
from Tool.gpt.unused_functions_prompt import unused_functions_prompt_task1, unused_functions_prompt_task2
from Tool.gpt.rename_variable_prompt import rename_variable_prompt_task1, rename_variable_prompt_task2
from Tool.gpt.format_prompt import format_code_prompt

class GPTidy:
    def __init__(self, notebook: Notebook):
        self.notebook = notebook
        self.introduction = None

    def generate_introduction(self):
        """
        Returns a string of the introduction
        """
        introduction = introduction_prompt(self.notebook)
        introduction = gpt_wrapper(introduction)
        finish_reason, result = gpt_unpack_simple(introduction)

        if finish_reason == 'stop':
            self.introduction = result
            return result
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def generate_summarize_cell(self, cell_id: int):
        """
        Returns a string of the code summary
        """
        if not self.introduction:
            self.generate_introduction()

        summarize_cell = summarize_cell_prompt(
            self.notebook, self.introduction, cell_id)
        summarize_cell = gpt_wrapper(summarize_cell)
        finish_reason, result = gpt_unpack_simple(summarize_cell)

        if finish_reason == 'stop':
            return result
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def generate_conclusion(self):
        """
        Returns a string of the conclusion
        """
        if not self.introduction:
            self.introduction = self.generate_introduction()

        conclusion = conclusion_prompt(self.notebook, self.introduction)
        conclusion = gpt_wrapper(conclusion)
        finish_reason, result = gpt_unpack_simple(conclusion)

        if finish_reason == 'stop':
            return result
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def remove_unused_variables(self, cell_id: int):
        """
        Returns a tuple of (unused_names, updated_code)
        """
        unused_variables_code = unused_variables_prompt(self.notebook, cell_id)
        unused_variables_code = gpt_wrapper(unused_variables_code)
        finish_reason, result = gpt_unpack_simple(unused_variables_code)

        if finish_reason == 'stop':
            # split the result into unused names and updated code
            result_split = result.split('Updated code:')
            # get the unused names
            unused_names = eval(result_split[0].split(
                'Unused variables:')[1].strip("\n"))
            # get the updated code
            updated_code = result_split[1].split('```')[1]
            if updated_code.startswith('python'):
                updated_code = updated_code[6:]
            updated_code = updated_code.strip('\n')
            # store
            if unused_names == []:
                raise Exception("Error: No unused variables found.")
            return unused_names, updated_code
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def remove_unused_functions(self, cell_id: int):
        """
        Returns a tuple of (unused_functions, new_code)
        """
        # part 1
        unused_functions_code_part1 = unused_functions_prompt_task1(
            self.notebook, cell_id)
        finish_reason, result1 = gpt_unpack_simple(
            gpt_wrapper(unused_functions_code_part1))

        # parse result
        if finish_reason == 'stop':
            try:
                res = eval(result1)
            except:
                raise Exception("Error: GPT-3.5 returned an invalid result.")
            else:
                if res == []:
                    raise Exception("Error: No unused functions found.")
                else:
                    result1 = res
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

        # part 2
        unused_functions_code_part2 = unused_functions_prompt_task2(
            self.notebook, cell_id, result1)
        finish_reason, result2 = gpt_unpack_simple(
            gpt_wrapper(unused_functions_code_part2))

        # parse result
        if finish_reason == 'stop':
            new = result2.split("```")
            if len(new) == 1:
                Exception("Error: GPT-3.5 returned an invalid result.")
            else:
                new = new[1]
                if new.startswith('python'):
                    new = new[6:].strip("\n")
            return result1, new
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def rename_variable(self, cell_id: int, name: str):
        """
        Returns a tuple of (new_name, explanation, updated_code)
        """

        # part 1
        rename_variable_code_part1 = rename_variable_prompt_task1(
            self.notebook, cell_id, name)
        finish_reason, result1 = gpt_unpack_simple(
            gpt_wrapper(rename_variable_code_part1))

        # parse result
        if finish_reason == 'stop':
            # split the result
            first_split = result1.split('New variable name:')[
                1].split('Explanation:')
            updated_name = first_split[0].strip()
            explanation = first_split[1].strip()

            # update name
            if len(updated_name.split('\'')) == 3:
                updated_name = updated_name.split('\'')[1]

            # update name
            if len(updated_name.split('`')) == 3:
                updated_name = updated_name.split('`')[1]

            # store
            gpt_new_name = updated_name
            gpt_explanation = explanation
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

        # part 2
        rename_variable_code_part2 = rename_variable_prompt_task2(
            self.notebook, cell_id, name, gpt_new_name)
        finish_reason, result2 = gpt_unpack_simple(
            gpt_wrapper(rename_variable_code_part2))

        # parse result
        if finish_reason == 'stop':
            updated_code = result2.split('```')[1]
            if updated_code.startswith('python'):
                updated_code = updated_code[6:]
            updated_code = updated_code.strip('\n')
            return gpt_new_name, gpt_explanation, updated_code
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")

    def rename_function(self, cell_id: int, name: str):
        """
        Returns a tuple of (new_name, explanation, updated_code)
        """

        # part 1
        rename_function_code_part1 = rename_function_prompt_task1(
            self.notebook, cell_id, name)
        finish_reason, result1 = gpt_unpack_simple(
            gpt_wrapper(rename_function_code_part1))

        # parse result
        if finish_reason == 'stop':
            # split the result
            first_split = result1.split('New function name:')[
                1].split('Explanation:')
            updated_name = first_split[0].strip()
            explanation = first_split[1].strip()

            # update name
            if len(updated_name.split('\'')) == 3:
                updated_name = updated_name.split('\'')[1]

            # update name
            if len(updated_name.split('`')) == 3:
                updated_name = updated_name.split('`')[1]

            # store
            gpt_new_name = updated_name
            gpt_explanation = explanation
        else:
            # if we error we assume nothing
            raise Exception("Error: GPT-3.5 returned an invalid result.")

        # part 2
        rename_function_code_part2 = rename_function_prompt_task2(
            self.notebook, cell_id, name, gpt_new_name)
        finish_reason, result2 = gpt_unpack_simple(
            gpt_wrapper(rename_function_code_part2))

        # parse result
        if finish_reason == 'stop':
            updated_code = result2.split('```')[1]
            if updated_code.startswith('python'):
                updated_code = updated_code[6:]
            updated_code = updated_code.strip('\n')
            return gpt_new_name, gpt_explanation, updated_code
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")
        
    
    def format_code(self, cell_id: int):
        """
        Returns a tuple of (code, changes)
        """
        format_code = format_code_prompt(self.notebook, cell_id)
        format_code = gpt_wrapper(format_code)
        finish_reason, result = gpt_unpack_simple(format_code)

        if finish_reason == 'stop':
            split = result['result'].split('Formatted code:')
            try:
                changes = split[0].split("Identified formatting issues:")[1].strip("\n")
            except:
                raise Exception("Error: GPT-3.5 returned an invalid result.")
            else:
                try:
                    code = split[1].split("```")[1].strip("\n")
                except:
                    raise Exception("Error: GPT-3.5 returned an invalid result.")
                else:
                    if code.startswith('python'):
                        code = code[6:].strip("\n")
                
            return code, changes
        else:
            raise Exception("Error: GPT-3.5 returned an invalid result.")


if __name__ == "__main__":
    # parse file
    if len(sys.argv) < 2:
        print("Usage: python3 gptidy.py <path to notebook>")
        sys.exit(1)
    file_path = sys.argv[1]

    # read in notebook using io
    with open(file_path, 'r') as f:
        notebook = json.load(f)

    notebook = Notebook(notebook)

    # ask for purpose
    purpose = input("What is the purpose of this notebook?")
    notebook.purpose = purpose

    gptidy = GPTidy(notebook)

    # ask the user what type of refactoring they want to do
    # markdown-related operations
    # 1. introduction
    # 2. summarize cell
    # 3. conclusion
    # code-related operations
    # 4. remove unused variables
    # 5. remove unused functions
    # 6. rename variable
    # 7. rename function
    # 8. format code
    # 9. exit
    while True:
        print("What type of refactoring would you like to do?")
        print("1. Introduction")
        print("2. Summarize cell")
        print("3. Conclusion")
        print("4. Remove unused variables")
        print("5. Remove unused functions")
        print("6. Rename variable")
        print("7. Rename function")
        print("8. Format code")
        print("9. Exit")
        choice = input("Enter a number: ")
        if choice == '1':
            print(gptidy.generate_introduction())
        elif choice == '2':
            cell_id = int(input("Enter the cell id: "))
            print(gptidy.generate_summarize_cell(cell_id))
        elif choice == '3':
            print(gptidy.generate_conclusion())
        elif choice == '4':
            cell_id = int(input("Enter the cell id: "))
            print(gptidy.remove_unused_variables(cell_id))
        elif choice == '5':
            cell_id = int(input("Enter the cell id: "))
            print(gptidy.remove_unused_functions(cell_id))
        elif choice == '6':
            cell_id = int(input("Enter the cell id: "))
            name = input("Enter the name of the variable: ")
            print(gptidy.rename_variable(cell_id, name))
        elif choice == '7':
            cell_id = int(input("Enter the cell id: "))
            name = input("Enter the name of the function: ")
            print(gptidy.rename_function(cell_id, name))
        elif choice == '8':
            cell_id = int(input("Enter the cell id: "))
            print(gptidy.format_code(cell_id))
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")