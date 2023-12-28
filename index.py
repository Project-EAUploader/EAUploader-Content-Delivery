import requests
import json
from datetime import datetime

def list_files(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/master?recursive=1"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    tree = response.json().get('tree', [])

    files = {}
    for item in tree:
        if item['type'] == 'blob':
            path = item['path']
            directory = '/'.join(path.split('/')[:-1])
            if directory not in files:
                files[directory] = []
            files[directory].append(item['url'])

    return files

def main():
    owner = 'GITHUB_OWNER'  # Replace with GitHub repository owner
    repo = 'GITHUB_REPO'    # Replace with GitHub repository name
    token = 'GITHUB_TOKEN'  # Replace with a GitHub token

    files = list_files(owner, repo, token)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = {
        'timestamp': timestamp,
        'files': files
    }

    with open('files_list.json', 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    main()
