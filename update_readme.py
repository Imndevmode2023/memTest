import os
import requests
import base64

def update_readme(token, repo_name, content):
    url = f"https://api.github.com/repos/{repo_name}/contents/README.md"
    headers = {
        "Authorization": f"token {token}"
    }
    
    # Fetch existing README to get its SHA
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Failed to fetch README: {r.json()}")
        return False
    
    sha = r.json().get('sha', None)
    if sha is None:
        print("SHA not found in the response.")
        return False
    
    # Update README
    data = {
        "message": "Update README.md",
        "content": base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        "sha": sha
    }
    r = requests.put(url, headers=headers, json=data)
    return r.status_code == 200

if __name__ == "__main__":
    # GitHub token from environment variables
    token = os.environ.get("GH_TOKEN")
    
    # Your GitHub username and repo name
    repo_name = "imndevmode2023/memTest"

    # New content for README.md
    new_content = "This is the updated content."

    # Update README.md
    if update_readme(token, repo_name, new_content):
        print("README updated successfully.")
    else:
        print("Failed to update README.")
