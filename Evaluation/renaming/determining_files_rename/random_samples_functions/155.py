import re

def function_def(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\\)|\\(|D|P)', text)
    text = re.sub('[\\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text