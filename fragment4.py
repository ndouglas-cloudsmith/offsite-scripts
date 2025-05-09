import time
import urllib.request

def download_reward():
    reward_url = "https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/reward4.txt"
    save_as = "reward4.txt"
    try:
        print("\n📥 Downloading your reward file...")
        urllib.request.urlretrieve(reward_url, save_as)
        print(f"✅ Reward downloaded as '{save_as}'!")
    except Exception as e:
        print(f"❌ Failed to download the reward: {e}")

def celebrate_success():
    print("🐾 Wow! I trust that you completed this task all on your own.")
    print("🎁 Downloading reward number 4 (No need for a flag this time, buddy.)...")
    time.sleep(1.5)
    download_reward()

if __name__ == "__main__":
    celebrate_success()
