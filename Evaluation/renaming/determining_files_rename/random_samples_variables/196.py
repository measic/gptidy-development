import re
CLASS_NAME_REGEX = re.compile('^n\\d+\\s+(.*)\\s*$', re.M | re.U)

def load_class_names():
    with open(os.path.join('datasets', 'inception', 'imagenet_class_names.txt'), 'rb') as f:
        variable_def = f.read().decode('utf-8')
        return CLASS_NAME_REGEX.findall(variable_def)