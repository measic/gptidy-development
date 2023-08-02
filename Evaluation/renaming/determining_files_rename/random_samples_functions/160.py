def function_def(url):
    try:
        result = http_program(url)
        return True
    except ValueError:
        return False