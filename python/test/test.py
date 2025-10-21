import time
import itertools
import os

# 💖 Infinite Happy Diwali Animation by Amit 💖

def print_pattern(emoji1, emoji2, text="happy", festival="diwali", delay=0.2):
    # Define the pattern structure
    lines = []

    # Top block
    for _ in range(3):
        lines.append(f"{emoji1}{text}{emoji2}{festival}{emoji1}")

    # Increasing hyphen pattern
    for i in range(1, 6):
        lines.append(f"{'-' * i}{emoji1}{text}{emoji2}{festival}{emoji1}")

    # Peak pattern (3 lines)
    for _ in range(3):
        lines.append(f"{'-' * 5}{emoji1}{text}{emoji2}{festival}{emoji1}")

    # Decreasing hyphen pattern
    for i in range(4, 0, -1):
        lines.append(f"{'-' * i}{emoji1}{text}{emoji2}{festival}{emoji1}")

    # Bottom block
    for _ in range(3):
        lines.append(f"{emoji1}{text}{emoji2}{festival}{emoji1}")

    # Print with delay
    for line in lines:
        print(line)
        time.sleep(delay)


def infinite_diwali():
    styles = [
        ('❤', '♥'),
        ('💚', '💚'),
        ('💜', '💜'),
        ('💖', '💖'),
        ('💙', '💙')
    ]

    print("💐💐💐 In Advance 💐💐💐\n")

    # Infinite loop
    for e1, e2 in itertools.cycle(styles):
        print_pattern(e1, e2, delay=0.1)  # change delay for faster/slower effect
        print()  # space between styles


# Run it
try:
    infinite_diwali()
except KeyboardInterrupt:
    os.system('clear' if os.name != 'nt' else 'cls')
    print("✨ Program stopped. Happy Diwali, Amit! ✨")
