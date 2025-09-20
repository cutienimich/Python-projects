import time
import pygame
import ctypes
import sys

# Initialize mixer
pygame.mixer.init()

# Lyrics and timing (console only)
lyrics = [
    ('...', 2),
    ("What if she's fine?", 2),
    ("It's my mind that's wrong", 2.6),
    ("And I just let bad thoughts", 3),
    ("Linger for far too long", 0.8)
]

# Display original lyrics twice (console only)
for repeat in range(2):
    print(f"\n--- Repeat {repeat + 1} ---\n")
    for line, duration in lyrics:
        print(line)
        time.sleep(duration)

# Function to type out text like it's being written
def type_text(text, delay=0.1):
    typed = ""
    for char in text:
        typed += char
        sys.stdout.write("\r" + typed)  # overwrite same line
        sys.stdout.flush()
        time.sleep(delay)
    print()  # new line after typing

# Dramatic "pleaaaase"
def stretch_word(base, stretch_count):
    return base + "a" * stretch_count + "se"

# New lyrics sequence
new_lyrics = [
    ("Don't you give me up", True),
    (stretch_word("ple", 4), False),   # console typing only
    ("don't give up, honey", True),
    ("I belong with you, and only you, babe", True)
]


for i, (line, show_popup) in enumerate(new_lyrics, start=1):
    if not show_popup: 
        
        type_text(line, 0.15)
    else:
        ctypes.windll.user32.MessageBoxW(0, line, f"Lyrics Line {i}", 0)
        time.sleep(0.5)  # optional pause between alerts
