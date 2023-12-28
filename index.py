import requests
import json
from datetime import datetime

def list_files(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/master?recursive=1"
    response = requests.get(url)
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
    owner = 'Project-EAUploader'
    repo = 'EAUploader-Content-Delivery'

    files = list_files(owner, repo)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = {
        'timestamp': timestamp,
        'files': files
    }

    with open('index.json', 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    main()
