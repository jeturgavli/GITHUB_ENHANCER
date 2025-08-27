# contribution_finder.py

import requests
from .token_manager import get_github_token  # Make sure token_manager.py exists and returns your GitHub token

def get_good_first_issues(repo_limit=5, topic=None):
    print(f"\n[INFO] Searching top {repo_limit} repositories with good first issues for topic: {topic}")

    query = "good-first-issues:>0"
    if topic:
        query += f" topic:{topic}"

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={repo_limit}"

    # Optional: Use GitHub token if available
    token = get_github_token()
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("[ERROR] Failed to fetch repositories:", e)
        return

    repos = data.get("items", [])

    if not repos:
        print("[WARNING] No repositories found.")
        return

    for index, repo in enumerate(repos, start=1):
        print(f"\n[{index}] Repository: {repo['full_name']}")
        print(f"    Stars     : {repo['stargazers_count']}")
        print(f"    URL       : {repo['html_url']}")
        print(f"    Topics    : {', '.join(repo.get('topics', [])) if repo.get('topics') else 'None'}")

        issues_url = repo['issues_url'].replace("{/number}", "")
        try:
            issues_response = requests.get(
                issues_url + "?labels=good%20first%20issue&state=open",
                headers=headers
            )
            issues_response.raise_for_status()
            issues = issues_response.json()
        except Exception as e:
            print("    [!] Failed to fetch issues:", e)
            continue

        if not issues:
            print("    [!] No good first issues found.")
            continue

        print("    Good First Issues:")
        for issue in issues[:3]:  # Show top 3 issues
            print(f"     - {issue['title']}")
            print(f"       {issue['html_url']}")


# === Main Program ===
if __name__ == "__main__":
    print("GitHub Good First Issue Finder")

    try:
        count = int(input("How many repositories per topic do you want to see? "))
        tags_input = input("Enter one or more topics (comma-separated, e.g., python,react,go): ").strip()
        topics = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        if not topics:
            print("No valid topics entered.")
        else:
            for topic in topics:
                print(f"\n========== Topic: {topic} ==========")
                get_good_first_issues(repo_limit=count, topic=topic)

    except ValueError:
        print("Invalid number entered.")

