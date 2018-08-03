"""This is a program to play a simple game of hangman with a certain number of guesses.
   Created by Eliano Anile."""

import random

GUESSED_LETTERS = set()              # Keep track of the user's guessed letters
WORDLIST_FILENAME = 'word_list.txt'  # Text file of 10,000 possible words


def load_words():
    """Function to load in words from a text file."""

    print("\nLoading word list from file...")
    # infile: file
    with open(WORDLIST_FILENAME, 'r') as infile:
        # wordlist: list of strings
        wordlist = []
        for line in infile:
            wordlist.append(line.rstrip('\n'))
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """Function to choose a random word from a wordlist."""

    return random.choice(wordlist)


def get_user_guess(num_guesses):
    """Function to get a valid user-inputted character."""

    while True:
        guess = input("Enter a letter to guess (%d guesses remaining): " % num_guesses).lower()

        # Checks if the input is a character
        if not(guess >= 'a' and guess <= 'z'):
            print("Please enter only letters.")
        # Checks if the input is more than one character
        elif len(guess) > 1:
            print("Please enter only one character.")
        # Checks if the user already guessed their input
        elif guess in GUESSED_LETTERS:
            print("You already guessed '{}'!".format(guess))
        else:
            GUESSED_LETTERS.add(guess)
            return guess


def play_hangman():
    """Function to play all the parts of hangman."""

    wordlist = load_words()                   # List that holds all possible words to guess
    word_to_guess = choose_word(wordlist)     # Chooses random word from wordlist
    user_guessed_word = ''                    # Used to check if the user has guessed the word
    hidden_word = ['_'] * len(word_to_guess)  # Displayed to the user and updated after each guess
    num_guesses = len(word_to_guess) + 4      # Number of guesses is greater than the character count in the word
    temp_guesses = num_guesses                # Used to iterate through a loop until game is finished

    # Prints the introductory text
    print("\nWELCOME TO HANGMAN!")
    print("You have a limited number of chances to guess the word.")
    print("You can only enter single characters.")

    # Loops until the user has no more guesses left
    while (temp_guesses > 0):

        # Prints the word hidden, except for the user's guesses
        print(' '.join(hidden_word))

        # Gets the user's guess
        user_guess = get_user_guess(temp_guesses)

        # Checks if the user's guess is in the word
        if user_guess in word_to_guess:
            print("The letter {} is in the word!\n".format(user_guess))

            # Updates the hidden word
            correct_guess = False
            for i, letter in enumerate(word_to_guess):
                if user_guess == letter:
                    correct_guess = True
                    hidden_word[i] = user_guess

            if correct_guess:
                temp_guesses += 1

            # Updates the user's guessed word (joined version of hidden word)
            user_guessed_word = ''.join(hidden_word)

        # Executes if the user's guess was not in the word
        else:
            print("The letter {} is not in the word!\n".format(user_guess))

        # Checks if the user has completely guessed the word
        if user_guessed_word == word_to_guess:
            print(' '.join(word_to_guess))
            return True

        temp_guesses -= 1

    # Executes after the loop has completed, meaning the user has run out of tries
    print("""Sorry, you did not guess the word "{}"!""".format(word_to_guess))
    return False

if __name__ == "__main__":

    winner = play_hangman()

    # Checks if the user won
    if winner:
        print("Congratulations! You guessed the word!")
    else:
        print("Game Over!")