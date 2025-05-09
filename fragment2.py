import getpass
import time
import urllib.request
import sys

# --- Password Protection ---
PASSWORD = "flag-kqE7a0Mr5Yld"

def download_reward():
    reward_url = "https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/reward2.txt"
    save_as = "reward2.txt"
    try:
        print("\n📥 Downloading your reward file...")
        urllib.request.urlretrieve(reward_url, save_as)
        print(f"✅ Reward downloaded as '{save_as}'!")
    except Exception as e:
        print(f"❌ Failed to download the reward: {e}")

def password_protected():
    print("🚪 To access the second fragment, you need to provide the hidden flag associated with the blocking policy.")
    user_input = getpass.getpass("Password: ")
    if user_input == PASSWORD:
        print("✅ Access granted. You found the correct flag!")
        time.sleep(1)
        download_reward()
    else:
        print("❌ Incorrect Flag. Access denied.")
        time.sleep(2)
        sys.exit(1)

if __name__ == "__main__":
    password_protected()
