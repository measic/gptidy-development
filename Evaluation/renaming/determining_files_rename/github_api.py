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

def fetch_github_project_info(url):
    user_info_full = fetch_user_info(url)
    readme_full = fetch_readme(url)
    project_info = {}

    if user_info_full is not None and (user_info_full['company'] or user_info_full['bio']):
        user_info = {}
        if user_info_full['company']:
            user_info['company'] = user_info_full['company']
        if user_info_full['bio']:
            user_info['bio'] = user_info_full['bio']
        project_info['user_info'] = user_info
    if readme_full is not None:
        project_info['readme'] = readme_full

    # if project_info contains any info, return it
    return project_info or None