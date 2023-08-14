# get unused data using vulture
import subprocess

def get_unused_data(NUM_FILES, SAMPLES_FOLDER_NAME, condition, failed_ids):
    unused = [[] for _ in range(NUM_FILES)]

    for i in range(NUM_FILES):
        if i in failed_ids:
            continue
        file_name = f'{SAMPLES_FOLDER_NAME}/{i}.py'

        # Run on each files
        result = subprocess.run(['vulture', file_name], capture_output=True, text=True)

        # Get the output and return code
        outputs = result.stdout.strip().split('\n')
        outputs = [line for line in outputs if line != '']

        # keep only the strings that contain as requested
        variable_func = lambda lst: [item for item in lst if 'unused variable' in item]
        function_func = lambda lst: [item for item in lst if 'unused function' in item or 'unused method' in item]
        
        if condition == 'variable':
            outputs = variable_func(outputs)
        elif condition == 'function':
            outputs = function_func(outputs)
        else:
            raise ValueError('condition must be either variable or function')

        for output in outputs:
            # Get the name
            name = output.split("\'")[1]
            # Store
            unused[i].append(name)
    
    return unused