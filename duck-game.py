import curses
import time
import random
import getpass
import sys

# --- Password Protection ---
PASSWORD = "SADIE-REG-2025"

def password_protected():
    print("🚪 Welcome to Duck Pong! Please enter the password to proceed.")
    user_input = getpass.getpass("Password: ")
    if user_input == PASSWORD:
        print("✅ Access granted! Get ready to play!")
        time.sleep(1)
    else:
        print("❌ Incorrect password. Access denied.")
        time.sleep(2)
        exit()

password_protected()

# --- Duck Pong Game ---
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Window size
    height, width = stdscr.getmaxyx()

    # Duck paddles
    duck1_y = height // 2
    duck2_y = height // 2
    paddle_size = 4

    # Ball
    ball_x = width // 2
    ball_y = height // 2
    ball_dx = random.choice([-1, 1])
    ball_dy = random.choice([-1, 1])

    score1 = 0
    score2 = 0

    while True:
        stdscr.clear()

        # Draw middle dashed line
        for y in range(height):
            if y % 2 == 0:
                stdscr.addch(y, width // 2, '|')

        # Draw ducks (paddles)
        for i in range(-paddle_size//2, paddle_size//2):
            if 0 <= duck1_y + i < height:
                stdscr.addstr(duck1_y + i, 2, "🦆")
            if 0 <= duck2_y + i < height:
                stdscr.addstr(duck2_y + i, width - 3, "🦆")

        # Draw ball
        stdscr.addstr(ball_y, ball_x, "o")

        # Draw score
        stdscr.addstr(0, width//4, f"Player 1: {score1}")
        stdscr.addstr(0, 3 * width//4 - 10, f"Player 2: {score2}")

        stdscr.refresh()

        key = stdscr.getch()

        # Player controls
        if key == ord('w') and duck1_y > 1:
            duck1_y -= 3
        elif key == ord('s') and duck1_y < height - 2:
            duck1_y += 3
        elif key == curses.KEY_UP and duck2_y > 1:
            duck2_y -= 3
        elif key == curses.KEY_DOWN and duck2_y < height - 2:
            duck2_y += 3
        elif key == ord('q'):
            break

        # Move ball twice per frame (double speed)
        for _ in range(2):
            ball_x += ball_dx
            ball_y += ball_dy

            # Ball collision with top/bottom walls
            if ball_y <= 0 or ball_y >= height-1:
                ball_dy *= -1

            # Ball collision with paddles
            if ball_x == 3:
                if duck1_y - paddle_size//2 <= ball_y <= duck1_y + paddle_size//2:
                    ball_dx *= -1
                else:
                    score2 += 1
                    ball_x = width // 2
                    ball_y = height // 2
                    ball_dx = random.choice([-1, 1])
                    ball_dy = random.choice([-1, 1])
                    time.sleep(1)

            if ball_x == width - 4:
                if duck2_y - paddle_size//2 <= ball_y <= duck2_y + paddle_size//2:
                    ball_dx *= -1
                else:
                    score1 += 1
                    ball_x = width // 2
                    ball_y = height // 2
                    ball_dx = random.choice([-1, 1])
                    ball_dy = random.choice([-1, 1])
                    time.sleep(1)

        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)
