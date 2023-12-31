import random

def main():
    """Entry point to Hangman"""
    hangman()

def hangman():
    word_list = ["apple", "banana", "cherry", "durain", "elderberry", "fig", "grapefruit"]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_" * len(word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower
        print(guess)
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try Again")
            continue

        if guess not in word:
            attempts -= 1 # attempts = attempts - 1
            print("Incorrect guess. You Have", attempts, "Attampts left")
        else:
            guessed_letters.append(guess)

        word_progress = ""
        for letter in word:
            word_progress += letter + ""
        else:
            word_progress += "_"

        print(word_progress)

        if "_" not in word_progress:
            print("Contgratulation! you have gueseed the word correctly.")
            return
        print(f"You ran out of attempts. The word was, ${word}")


if __name__ == "__main__":
    main()