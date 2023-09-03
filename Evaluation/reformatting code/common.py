IGNORE_TYPES = 'W292,W391,E901,E902,W605,W503'

import subprocess

def unpack_gpt(gpt_results):
    gpt_formatted_code = []
    gpt_changes = []

    # get all the code from the results
    for i, result in enumerate(gpt_results):
        if gpt_results[i]['reason'] == 'stop':
            split = result['result'].split('Formatted code:')
            try:
                changes = split[0].split("Identified formatting issues:")[1].strip("\n")
            except:
                changes = None
                code = None
            else:
                try:
                    code = split[1].split("```")[1].strip("\n")
                except:
                    code = None
                else:
                    if code.startswith('python'):
                        code = code[6:].strip("\n")
                
            gpt_formatted_code.append(code)
            gpt_changes.append(changes)
        else:
            gpt_formatted_code.append(None)
            gpt_changes.append(None)
    
    return gpt_formatted_code, gpt_changes

# read in error type groups
# file has two columns: error_type, description, read this in as a hash
with open('../pep8_error_types.csv', 'r') as f:
    error_types = {}
    for line in f:
        error_type, description = line.strip().split(',')
        error_types[error_type] = description


def pycodestyle(folder_name, NUM_FILES, ignore_types):
    error_counts = {}

    for i in range(NUM_FILES):
        file_name = f'{folder_name}/{i}.py'
        result = subprocess.run(
            ['pycodestyle', f'--ignore={ignore_types}', '--statistics', file_name], stdout=subprocess.PIPE).stdout.decode('utf-8')
        result = result.split('\n')
        # keep only the lines that start with an integer
        result = [line for line in result if line and line[0].isdigit()]
        # store the error counts in a hash
        for line in result:
            error_type = line.split()[1]
            error_count = int(line.split()[0])
            if error_type in error_counts:
                error_counts[error_type] += error_count
            else:
                error_counts[error_type] = error_count
    return error_counts


def group_by_error(error_counts):
    # count the number of errors in each group that begins with an error type
    error_counts_grouped = {}
    for error_type, _ in error_types.items():
        error_counts_grouped[error_type] = 0
        for error, count in error_counts.items():
            if error.startswith(error_type):
                error_counts_grouped[error_type] += count

    return error_counts_grouped


def print_num_reductions(error_counts_before_grouped, error_counts_after_grouped):
    # number of reductions (negative is reduction, positive is increase)
    for error_type, description in error_types.items():
        print(
            f'{error_type, description}: {error_counts_before_grouped[error_type]} -> {error_counts_after_grouped[error_type]}')


def print_percentage_difference(error_counts_before_grouped, error_counts_after_grouped):
    # print the percentage difference
    for error_type, description in error_types.items():
        if error_counts_before_grouped[error_type] == 0:
            print(f'{error_type, description}: Undefined')
        else:
            percent_change = round(
                (error_counts_after_grouped[error_type] - error_counts_before_grouped[error_type]) / error_counts_before_grouped[error_type] * 100, 2)
            print(f'{error_type, description}: {percent_change}%')
