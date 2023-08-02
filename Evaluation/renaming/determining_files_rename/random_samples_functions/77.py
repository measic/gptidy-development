import re
CLASS_NAME_REGEX = re.compile('^n\\d+\\s+(.*)\\s*$', re.M | re.U)

def function_def():
    with open(os.path.join('datasets', 'inception', 'imagenet_class_names.txt'), 'rb') as f:
        content = f.read().decode('utf-8')
        return CLASS_NAME_REGEX.findall(content)