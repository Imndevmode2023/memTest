import os
import requests

def update_readme(token, repo_name, content):
    url = f"https://api.github.com/repos/{repo_name}/contents/README.md"
    headers = {
        "Authorization": f"token {token}"
    }
    
    # Fetch existing README to get its SHA
    r = requests.get(url, headers=headers)
    sha = r.json()['sha']
    
    # Update README
    data = {
        "message": "Update README.md",
        "content": content.encode('utf-8').base64encode(),
        "sha": sha
    }
    r = requests.put(url, headers=headers, json=data)
    return r.status_code == 200

if __name__ == "__main__":
    # GitHub token and repo name from environment variables
    token = os.environ.get("GH_TOKEN")
    repo_name = "memTest"

    # New content for README.md
    new_content = "This is the updated content."

    # Update README.md
    if update_readme(token, repo_name, new_content):
        print("README updated successfully.")
    else:
        print("Failed to update README.")
