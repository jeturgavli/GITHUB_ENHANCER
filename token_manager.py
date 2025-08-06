<<<<<<< HEAD
=======
<<<<<<< HEAD
# token_manager.py

=======
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
def get_github_token():
    try:
        with open(".token", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
<<<<<<< HEAD
        print("Error: .token file not found.")
        return None
=======
<<<<<<< HEAD
        print("❌ .token file nahi mili.")
        return None
=======
        print("Error: .token file not found.")
        return None
>>>>>>> c5e3911 (Removed all emojis and cleaned up code)
>>>>>>> 2c39e02 (Initial project files and README added)
