from github_summary import show_github_summary
from contribution_finder import find_repos_with_open_issues

def menu():
    while True:
<<<<<<< HEAD
        print("\nGitHub Enhancer Menu")
=======
<<<<<<< HEAD
        print("\n📘 GitHub Enhancer Menu")
=======
        print("\nGitHub Enhancer Menu")
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
        print("-" * 40)
        print("1. Show GitHub Summary")
        print("2. Contribution Finder")
        print("3. Exit")
<<<<<<< HEAD
        choice = input("Choose option (1-3): ").strip()
=======
<<<<<<< HEAD
        choice = input("🔸 Choose option (1-4): ").strip()
=======
        choice = input("Choose option (1-3): ").strip()
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)

        if choice == "1":
            show_github_summary()
        
        elif choice == "2":
<<<<<<< HEAD
=======
<<<<<<< HEAD
            lang = input("Kitne repositories chahiye? Enter an integer: ").strip()
            num = int(lang) if lang.isdigit() and int(lang)>0 else 10
            lang_name = input("Kaunsi programming language? (example: Python, JavaScript): ").strip()
            find_repos_with_open_issues(lang_name, num)
            
        elif choice == "2":
>>>>>>> 2c39e02 (Initial project files and README added)
            try:
                count = int(input("How many repositories do you want? Enter an integer: ").strip())
            except ValueError:
                print("Invalid number. Defaulting to 10.")
                count = 10

            language = input("Which programming language? (example: Python, JavaScript): ").strip()
            find_repos_with_open_issues(language, count)

        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
<<<<<<< HEAD
    menu()
=======
    menu()
=======
            try:
                count = int(input("How many repositories do you want? Enter an integer: ").strip())
            except ValueError:
                print("Invalid number. Defaulting to 10.")
                count = 10

            language = input("Which programming language? (example: Python, JavaScript): ").strip()
            find_repos_with_open_issues(language, count)

        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
