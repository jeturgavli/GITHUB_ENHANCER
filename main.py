from github_summary import show_github_summary
from contribution_finder import find_repos_with_open_issues

def menu():
    while True:
        print("\n📘 GitHub Enhancer Menu")
        print("-" * 40)
        print("1. Show GitHub Summary")
        print("2. Contribution Finder")
        print("3. Exit")
        choice = input("🔸 Choose option (1-4): ").strip()

        if choice == "1":
            show_github_summary()
        
        elif choice == "2":
            lang = input("Kitne repositories chahiye? Enter an integer: ").strip()
            num = int(lang) if lang.isdigit() and int(lang)>0 else 10
            lang_name = input("Kaunsi programming language? (example: Python, JavaScript): ").strip()
            find_repos_with_open_issues(lang_name, num)
            
        elif choice == "2":
            try:
                count = int(input("🔢 Kitne repositories chahiye? Enter an integer: ").strip())
            except ValueError:
                print("❌ Invalid number. Defaulting to 10.")
                count = 10

            language = input("💻 Kaunsi programming language? (example: Python, JavaScript): ").strip()
            find_repos_with_open_issues(language, count)


        elif choice == "3":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Galat choice, try again!")

if __name__ == "__main__":
    menu()
