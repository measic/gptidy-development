# get unused data using vulture
import subprocess

def get_unused_data(NUM_FILES, SAMPLES_FOLDER_NAME, condition):
    unused = [[] for _ in range(NUM_FILES)]

    for i in range(NUM_FILES):
        file_name = f'{SAMPLES_FOLDER_NAME}/{i}.py'

        # Run on each files
        result = subprocess.run(['vulture', file_name], capture_output=True, text=True)

        # Get the output and return code
        outputs = result.stdout.strip().split('\n')
        outputs = [line for line in outputs if line != '']
        outputs = [item.split(":")[2] for item in outputs]

        if condition == 'variable':
            outputs = [item for item in outputs if 'unused variable' in item]
        elif condition == 'function':
            outputs = [item for item in outputs if 'unused function' in item or 'unused method' in item]
        else:
            raise ValueError('condition must be either variable or function')

        for output in outputs:
            # Get the name
            name = output.split("\'")[1]
            # Store
            unused[i].append(name)
    
    return unused