import os
import time
import urllib.request
import ssl  # <-- Added!

# --- SSL Quick Fix (skip certificate verification) ---
ssl._create_default_https_context = ssl._create_unverified_context

# Sprite Mapping
sprites = {
    "wall": "🧱",
    "empty": "⬜",
    "dog": "🐕",
    "cloudsmith_office": "🏢",
    "treat": "🦴",
    "obstacle": "🧹"
}

# Map Layout
raw_map = [
    list("#############"),
    list("#L..T#T.#...#"),
    list("#.#.*.#...#.#"),
    list("#.T.....*T#.O"),
    list("#############")
]

# Game state
bones_collected = 0
total_bones = 4

# Find Sadie's start position
for y, row in enumerate(raw_map):
    for x, tile in enumerate(row):
        if tile == 'L':
            player_x, player_y = x, y

def print_map():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen
    print(f"🦴 Bones collected: {bones_collected}/{total_bones}\n")
    for row in raw_map:
        for tile in row:
            if tile == '#':
                print(sprites["wall"], end="")
            elif tile == '.':
                print(sprites["empty"], end="")
            elif tile == 'L':
                print(sprites["dog"], end="")
            elif tile == 'O':
                print(sprites["cloudsmith_office"], end="")
            elif tile == 'T':
                print(sprites["treat"], end="")
            elif tile == '*':
                print(sprites["obstacle"], end="")
        print()

def download_reward():
    reward_url = "https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/game2.txt"
    save_as = "reward.txt"
    try:
        print("\n📥 Downloading your reward file...")
        urllib.request.urlretrieve(reward_url, save_as)
        print(f"✅ Reward downloaded as '{save_as}'!")
    except Exception as e:
        print(f"❌ Failed to download the reward: {e}")

def move_player(dx, dy):
    global player_x, player_y, bones_collected
    new_x = player_x + dx
    new_y = player_y + dy
    target_tile = raw_map[new_y][new_x]
    
    if target_tile in ['.', 'O', 'T']:
        if target_tile == 'T':
            bones_collected += 1
            print("🦴 Yum! Sadie got a bone!")
            time.sleep(2)
        
        if target_tile == 'O':
            if bones_collected == total_bones:
                print("\n🎉🐕 VICTORY! 🐕🎉")
                print("Sadie has collected all the bones and arrived at the Cloudsmith offsite!\n")
                print("""
       (•‿•)
      /      \\
     /        \\ 
    |  🦴  🦴 |
    \\  🦴  🦴 /
     \\______/
     
She's wagging her tail happily! 🎈
""")
                download_reward()
                time.sleep(3)
                exit()
            else:
                print(f"🚪 The office is locked! Sadie needs {total_bones - bones_collected} more bone(s) to join offsite!")
                time.sleep(2)
                return  # Don't allow moving into the office yet
        
        # Move the player
        raw_map[player_y][player_x] = '.'  # Leave empty space
        player_x, player_y = new_x, new_y
        raw_map[player_y][player_x] = 'L'
    
    elif target_tile == '*':
        print("😱 Sadie dislikes vacuum cleaners!")
        time.sleep(2)

    elif target_tile == '#':
        print("🚫 Oops! There's a wall there!")
        time.sleep(2)

# --- Game Loop ---
while True:
    print_map()
    move = input("Move (WASD): ").lower()
    if move == 'w':
        move_player(0, -1)
    elif move == 's':
        move_player(0, 1)
    elif move == 'a':
        move_player(-1, 0)
    elif move == 'd':
        move_player(1, 0)
    else:
        print("🔤 Use W, A, S, D to move!")
