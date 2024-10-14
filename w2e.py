import time
import sys

# ANSI escape code for yellow text
YELLOW = "\033[93m"
RESET = "\033[0m"

# Lyrics stored as a string
lyrics = """
You'd call me a loser, oh
Why won't you compromise?
I'd rather give you an F
Fuck you, I am saying
"""

# Function to display lyrics as running text with yellow color
def running_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(YELLOW + char + RESET)  # Print each character in yellow
        sys.stdout.flush()  # Ensure it's printed immediately
        time.sleep(delay)   # Delay between each character

# Call the function with the lyrics
running_text(lyrics, delay=0.1)  # Adjust delay to control speed
