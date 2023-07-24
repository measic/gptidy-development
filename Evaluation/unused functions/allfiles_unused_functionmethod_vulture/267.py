def is_valid_url(url):
    try:
        result = http_program(url)
        return True
    except ValueError:
        return False