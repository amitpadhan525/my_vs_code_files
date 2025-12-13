# EXACT pattern from your image

rows = [
    10,  # row 1
    9,   # row 2
    8,   # row 3
    7,   # row 4 (split shape begins)
    4,   # row 5 left stars
    2    # row 6 left stars
]

def exact_pattern():
    spaces = 0
    for r in rows:
        print(" " * spaces + "* " * r)
        spaces += 1

exact_pattern()
