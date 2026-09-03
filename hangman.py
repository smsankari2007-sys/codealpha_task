import random

print("🎮 Welcome to Hangman Game")

# Word list
words = ["python", "apple", "college", "project"]
word = random.choice(words)

guessed = ""
attempts = 5

while attempts > 0:
    display = ""

    # Show word progress
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win
    if "_" not in display:
        print("🎉 You Win!")
        break

    # User input
    guess = input("Enter a letter: ")

    # Add guessed letter
    guessed += guess

    # Wrong guess
    if guess not in word:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

# If lost
if attempts == 0:
    print("💀 You Lost! Word was:", word)