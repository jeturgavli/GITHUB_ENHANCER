# main.py

import requests
from .token_manager import get_github_token  # import token function

def make_request(url, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response

def get_user_data(username, token):
    user_url = f"https://api.github.com/users/{username}"
    response = make_request(user_url, token)
    if response.status_code == 200:
        return response.json()
    else:
        print("User not found ya API error.")
        return None

def get_repo_data(username, token):
    repos = []
    page = 1
    while True:
        repo_url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = make_request(repo_url, token)
        if response.status_code != 200:
            print("Repo fetch karne me dikkat aayi.")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def show_github_summary():
    token = get_github_token()
    if not token:
        return

    username = input("GitHub username daalo: ").strip()
    user_data = get_user_data(username, token)
    
    if not user_data:
        return

    repos = get_repo_data(username, token)
    total_repos = len(repos)
    forked_repos = sum(1 for repo in repos if repo.get("fork"))

    print("-"*35)
    print("Summary:")
    print("-"*35)
    print(f"Username: {username}")
    print(f"Total Repositories: {total_repos}")
    print(f"Forked Repositories: {forked_repos}")
    print(f"Followers: {user_data.get('followers')}")
    print(f"Following: {user_data.get('following')}")

if __name__ == "__main__":
    main()

