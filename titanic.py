import os
import time
import random
import getpass

# --- Password Protection ---
PASSWORD = "696zN:;w{"

def password_protected():
    print("🚪 Welcome to Sadie's Titanic Adventure! Please enter the password to proceed.")
    user_input = getpass.getpass("Password: ")
    if user_input == PASSWORD:
        print("✅ Access granted! Get ready to set sail!")
        time.sleep(1)
        return True
    else:
        print("❌ Incorrect password. Access denied.")
        time.sleep(2)
        exit()

# --- Game Settings ---
WIDTH = 20
HEIGHT = 10
player_pos = WIDTH // 2
icebergs = []
packages = []
collected_packages = 0
needed_packages = 10
frame_count = 0
game_over = False

# --- Sprites ---
SPRITE_EMPTY = "⬜"
SPRITE_TITANIC = "🚢"
SPRITE_ICEBERG = "🧊"
SPRITE_PACKAGE = "📦"

def print_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Build the screen
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) in icebergs:
                row += SPRITE_ICEBERG
            elif (x, y) in packages:
                row += SPRITE_PACKAGE
            elif y == HEIGHT - 1 and x == player_pos:
                row += SPRITE_TITANIC
            else:
                row += SPRITE_EMPTY
        print(row)
    print(f"\n📦 Packages collected: {collected_packages}/{needed_packages}")
    print("Move with A (left) and D (right). Avoid icebergs and collect packages! ❄️📦")

def update_icebergs():
    global game_over
    new_icebergs = []
    for x, y in icebergs:
        if y + 1 == HEIGHT - 1 and x == player_pos:
            game_over = True
        elif y + 1 < HEIGHT:
            new_icebergs.append((x, y + 1))
    return new_icebergs

def update_packages():
    new_packages = []
    for x, y in packages:
        if y + 1 < HEIGHT:
            new_packages.append((x, y + 1))
    return new_packages

def add_iceberg():
    x = random.randint(0, WIDTH - 1)
    icebergs.append((x, 0))

def add_package():
    x = random.randint(0, WIDTH - 1)
    packages.append((x, 0))

def victory_screen():
    print("\n🏆🎉 YOU WIN! 🎉🏆")
    print("Sadie successfully collected all the software packages!")
    print("""
        🚢 ~ ~ ~ 🌊
          ~ 🌊 ~ ~
        🌊 ~ 🚢 ~ 🌊
          ~ ~ ~ 🌊
    """)
    # Create reward2.txt with the registration code
    with open("reward2.txt", "w") as file:
        file.write("Registration Code for Game 3: SADIE-REG-2025")
    print("\n🔑 A reward2.txt file has been created with your registration code!")

    # Download the extra file
    print("\n⬇️ Downloading a special bonus file for you...")
    os.system('wget https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/duck-game.py')
    print("\n✅ Download complete! Check your folder for duck-game.py!")

    time.sleep(5)
    exit()

# --- Main Game Loop ---
if password_protected():
    while not game_over:
        print_screen()

        # Player Move
        move = input("Move (A/D): ").lower()
        if move == 'a' and player_pos > 0:
            player_pos -= 1
        elif move == 'd' and player_pos < WIDTH - 1:
            player_pos += 1

        # Check package collection
        collected_now = []
        for x, y in packages:
            if y == HEIGHT - 1 and x == player_pos:
                collected_now.append((x, y))

        for p in collected_now:
            packages.remove(p)
            collected_packages += 1

        # Victory Condition
        if collected_packages >= needed_packages:
            print_screen()
            victory_screen()

        # Update Icebergs and Packages
        icebergs = update_icebergs()
        packages = update_packages()

        # Add new icebergs every 3 frames
        if frame_count % 3 == 0:
            add_iceberg()

        # Add new packages every 5 frames
        if frame_count % 5 == 0:
            add_package()

        frame_count += 1

    # Game Over
    print_screen()
    print("\n💥🚢 Oh no! Sadie hit an iceberg! Game Over!")
    time.sleep(3)
