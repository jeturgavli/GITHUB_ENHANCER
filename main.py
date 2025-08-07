from github_summary import show_github_summary
from contribution_finder import get_good_first_issues  # Correct function

def menu():
    while True:
        print("\nGitHub Enhancer Menu")
        print("-" * 40)
        print("1. Show GitHub Summary")
        print("2. Contribution Finder")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            show_github_summary()

        elif choice == "2":
            try:
                count = int(input("How many repositories per topic? ").strip())
            except ValueError:
                print("Invalid number. Using default: 10")
                count = 10

            tags_input = input("Enter one or more topics (comma-separated, e.g., python,react): ").strip()
            topics = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            
            if not topics:
                print("No valid topics entered.")
            else:
                for topic in topics:
                    print(f"\nTopic: {topic}")
                    get_good_first_issues(repo_limit=count, topic=topic)

        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
