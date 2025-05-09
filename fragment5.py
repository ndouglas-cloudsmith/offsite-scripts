#    __    __
#  o-''))_____\\
#  "--__/ * * * )
#  c_c__/-c____/
#
# 🛑 Do not read this script — the contents are forbidden.
# The answers lie not in the code, but in the clues you've been given.
# Resist the urge. Proceed as instructed by the ASCII Dogs. 👁️

import time
import urllib.request
import sys

def download_reward():
    reward_url = "https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/reward1.txt"
    save_as = "reward1.txt"
    try:
        print("\n📥 Downloading your reward file...")
        urllib.request.urlretrieve(reward_url, save_as)
        print(f"✅ Reward downloaded as '{save_as}'!")
    except Exception as e:
        print(f"❌ Failed to download the reward: {e}")

def ask_questions():
    print("🐕 Welcome, seeker. Only the wise shall proceed.")
    
    year = input("📅 What year was the song published? ")
    if year.strip() != "2017":
        print("❌ That doesn’t sound right. You must look deeper.")
        sys.exit(1)

    rate = input("🎧 What is the sampling rate? ")
    valid_answers = {"44", "44.1", "44.1 kHz"}
    if rate.strip().lower() not in {v.lower() for v in valid_answers}:
        print("❌ Incorrect sampling rate. Listen more closely.")
        sys.exit(1)

    print("✅ You have answered wisely. The Bone of Eternity is yours.")
    time.sleep(1)
    download_reward()

if __name__ == "__main__":
    ask_questions()
