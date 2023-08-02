import re
variable_def = re.compile('^n\\d+\\s+(.*)\\s*$', re.M | re.U)

def load_class_names():
    with open(os.path.join('datasets', 'inception', 'imagenet_class_names.txt'), 'rb') as f:
        content = f.read().decode('utf-8')
        return variable_def.findall(content)