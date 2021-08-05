import random


def play_hangman():

    welcome()
    secret_word = random_secret_word()
    guessed_letters = right_letters(secret_word)

    hanged = False
    got_it_right = False 
    mistakes = 0

    while(not hanged and not got_it_right):
        guess = input("\nWhich Letter? ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            sets_the_right_guess(secret_word, guessed_letters, guess)
        else:
            mistakes += 1
            hangman_art(mistakes)
            print(f"You made {mistakes} mistakes.")

        if (mistakes == 7):
            break

        got_it_right = "_" not in guessed_letters
        print(guessed_letters)

    if (got_it_right):
        print("Congrats you won!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Ohh no, you died!")
        print("The word was {}".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


# functions

def welcome():
    print("\n****************************")
    print("Welcome to the hangman game!")
    print("****************************")


def random_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file: 
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def right_letters(secret_word):
    return ["_" for letter in secret_word]


def sets_the_right_guess(secret_word, guessed_letters, guess):
    index = 0
    for letter in secret_word:
        if(guess == letter):
            guessed_letters[index] = letter
        index += 1


def hangman_art(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# run the file, since it is in a "bigger one" AKA "all_games.py"
if(__name__ == "__main__"): 
    play_hangman()
