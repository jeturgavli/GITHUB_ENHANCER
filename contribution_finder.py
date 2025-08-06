# contribution_finder.py

import requests
from token_manager import get_github_token

def search_repositories(language, per_page, token):
    headers = {"Authorization": f"token {token}"}
    # ✔ Use issues:>0 to only get repos with open issues
    query = f"language:{language} is:public issues:>0"
    url = f"https://api.github.com/search/repositories?q={query}&sort=updated&order=desc&per_page={per_page}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print("❌ Repo search request failed.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return []

def find_repos_with_open_issues(language, count):
    token = get_github_token()
    if not token:
        print("❌ GitHub token missing.")
        return

    repos = search_repositories(language, count, token)
    if not repos:
        print(f"📭 No repositories found with open issues in {language}.")
        return

    output_lines = []
    for repo in repos:
        full_name = repo.get("full_name", "Unknown")
        issues = repo.get("open_issues_count", 0)
        url = repo.get("html_url", "") + "/issues"

        output_lines.append(f"✅ Repo: {full_name}")
        output_lines.append(f"🔢 Open Issues: {issues}")
        output_lines.append(f"🔗 Link: {url}")
        output_lines.append("-" * 60)

    # Join all lines into a single string
    output = "\n".join(output_lines)

    # Show output to user
    print("\n📦 Repositories with Open Issues:")
    print(output)

    # Ask if user wants to save
    choice = input("\n📝 Do you want to save this output to a text file? (y/n): ").strip().lower()
    if choice == 'y':
        filename = f"repos_with_issues_{language}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"✅ Output saved to {filename}")
        except Exception as e:
            print("❌ Failed to save file:", e)
    else:
        print("📄 Output not saved.")
