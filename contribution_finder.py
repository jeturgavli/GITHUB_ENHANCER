<<<<<<< HEAD
=======
<<<<<<< HEAD
# contribution_finder.py

=======
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
import requests
from token_manager import get_github_token

def search_repositories(language, per_page, token):
    headers = {"Authorization": f"token {token}"}
<<<<<<< HEAD
=======
<<<<<<< HEAD
    # ✔ Use issues:>0 to only get repos with open issues
=======
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
    query = f"language:{language} is:public issues:>0"
    url = f"https://api.github.com/search/repositories?q={query}&sort=updated&order=desc&per_page={per_page}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("items", [])
    else:
<<<<<<< HEAD
        print("Error: Repository search request failed.")
=======
<<<<<<< HEAD
        print("❌ Repo search request failed.")
=======
        print("Error: Repository search request failed.")
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return []

def find_repos_with_open_issues(language, count):
    token = get_github_token()
    if not token:
<<<<<<< HEAD
        print("Error: GitHub token missing.")
=======
<<<<<<< HEAD
        print("❌ GitHub token missing.")
=======
        print("Error: GitHub token missing.")
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
        return

    repos = search_repositories(language, count, token)
    if not repos:
<<<<<<< HEAD
        print(f"No repositories found with open issues in {language}.")
=======
<<<<<<< HEAD
        print(f"📭 No repositories found with open issues in {language}.")
=======
        print(f"No repositories found with open issues in {language}.")
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
        return

    output_lines = []
    for repo in repos:
        full_name = repo.get("full_name", "Unknown")
        issues = repo.get("open_issues_count", 0)
        url = repo.get("html_url", "") + "/issues"

<<<<<<< HEAD
        output_lines.append(f"Repository: {full_name}")
        output_lines.append(f"Open Issues: {issues}")
        output_lines.append(f"Link: {url}")
=======
<<<<<<< HEAD
        output_lines.append(f"✅ Repo: {full_name}")
        output_lines.append(f"🔢 Open Issues: {issues}")
        output_lines.append(f"🔗 Link: {url}")
>>>>>>> 2c39e02 (Initial project files and README added)
        output_lines.append("-" * 60)

    output = "\n".join(output_lines)

    print("\nRepositories with Open Issues:")
    print(output)

<<<<<<< HEAD
    choice = input("\nDo you want to save this output to a text file? (y/n): ").strip().lower()
=======
    # Ask if user wants to save
    choice = input("\n📝 Do you want to save this output to a text file? (y/n): ").strip().lower()
=======
        output_lines.append(f"Repository: {full_name}")
        output_lines.append(f"Open Issues: {issues}")
        output_lines.append(f"Link: {url}")
        output_lines.append("-" * 60)

    output = "\n".join(output_lines)

    print("\nRepositories with Open Issues:")
    print(output)

    choice = input("\nDo you want to save this output to a text file? (y/n): ").strip().lower()
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
    if choice == 'y':
        filename = f"repos_with_issues_{language}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
<<<<<<< HEAD
            print(f"Output saved to {filename}")
=======
<<<<<<< HEAD
            print(f"✅ Output saved to {filename}")
>>>>>>> 2c39e02 (Initial project files and README added)
        except Exception as e:
            print("Error: Failed to save file:", e)
    else:
<<<<<<< HEAD
        print("Output not saved.")
=======
        print("📄 Output not saved.")
=======
            print(f"Output saved to {filename}")
        except Exception as e:
            print("Error: Failed to save file:", e)
    else:
        print("Output not saved.")
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
