import random

# List of words
words = ["python", "computer", "developer", "coding", "program"]

# Select random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect attempts.\n")


while attempts > 0:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break


    # User input
    guess = input("Enter a letter: ").lower()


    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue


    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue


    guessed_letters.append(guess)


    # Correct or wrong guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)


# Lose condition
if attempts == 0:
    print("\n😢 Game Over!")
    print("The correct word was:", word)