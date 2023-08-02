import sys
import platform
from importlib.util import find_spec, module_from_spec

def function_def(version_inst, version_nec):
    version_inst_split = version_inst.split('.')
    version_nec_split = version_nec.split('.')
    for i in range(min(len(version_inst_split), len(version_nec_split))):
        if int(version_nec_split[i]) > int(version_inst_split[i]):
            return False
        elif int(version_nec_split[i]) < int(version_inst_split[i]):
            return True
    return True
module_list = [('jupyter', '1.0.0'), ('matplotlib', '2.0.2'), ('numpy', '1.13.1'), ('python', '3.6.2'), ('sklearn', '0.19.0'), ('scipy', '0.19.1'), ('nb_conda', '2.2.1')]
packages_correct = True
packages_errors = []
for module_name, version in module_list:
    if module_name == 'scikit-learn':
        module_name = 'sklearn'
    if module_name == 'pyyaml':
        module_name = 'yaml'
    if 'python' in module_name:
        python_version = platform.python_version()
        if not function_def(python_version, version):
            packages_correct = False
            error = f'Update {module_name} to version {version}. Current version is {python_version}.'
            packages_errors.append(error)
            print(error)
    else:
        spec = find_spec(module_name)
        if spec is None:
            packages_correct = False
            error = f'Install {module_name} with version {version} or newer, it is required for this assignment!'
            packages_errors.append(error)
            print(error)
        else:
            x = __import__(module_name)
            if hasattr(x, '__version__') and (not function_def(x.__version__, version)):
                packages_correct = False
                error = f'Update {module_name} to version {version}. Current version is {x.__version__}.'
                packages_errors.append(error)
                print(error)
try:
    from google.colab import drive
    packages_correct = False
    error = "Please, don't use google colab!\nIt will make it much more complicated for us to check your homework as it merges all the cells into one."
    packages_errors.append(error)
    print(error)
except:
    pass
packages_errors = '\n'.join(packages_errors)