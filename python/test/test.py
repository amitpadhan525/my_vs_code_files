
# Define the heart patterns for each color
colors = ["❤", "💚", "💜", "💖", "💙"]
lines = [
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
    "Ananya I{}You{}",
       ]
def print_pattern(color):
    # Top part
    for i in range(3):
        print(f"{color}happy{color}diwali{color}")
    # Pyramid top
    for i in range(1, 6):
        print(f"{'-'*i}{color}happy{color}diwali{color}")
    # Pyramid bottom
    for i in range(5, 0, -1):
        print(f"{'-'*i}{color}happy{color}diwali{color}")
    # Bottom part
    for i in range(3):
        print(f"{color}happy{color}diwali{color}")

# Print the pattern for each color
for color in colors:
    print_pattern(color)
