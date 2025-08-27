# token_manager.py

def get_github_token():
    try:
        with open(".token", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(".token file nahi mili.")
        return None
