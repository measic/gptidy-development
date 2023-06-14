import requests


def fetch_response_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def fetch_response_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def fetch_readme(url):
    # first try to get readme from this commit
    split_url = url.split('/')
    split_url = split_url[:6] + ['README.md']
    readme_url = '/'.join(split_url)
    readme = fetch_response_text(readme_url)
    if not readme:
        split_url[5] = 'master'
        readme_url = '/'.join(split_url)
        readme = fetch_response_text(readme_url)
        if not readme:
            split_url[5] = 'main'
            readme_url = '/'.join(split_url)
            readme = fetch_response_text(readme_url)
    return readme


def fetch_user_info(url):
    username = url.split('/', 4)[3]
    url = f"https://api.github.com/users/{username}"
    return fetch_response_json(url)


def fetch_notebook(url):
    return fetch_response_json(url)
