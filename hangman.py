import random

    print("\n****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    # para cada letra na palavra adicione no final da lista "_"
    guessed_letters = ["_" for letter in secret_word]

    hanged = False
    got_it_right = False  # O jogo ainda não começou por isso deixamos "False"
    mistakes = 0

    while(not hanged and not got_it_right):  # Enquanto(True and True) = Enquanto(True)
        guess = input("\nWhich Letter? ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
            # você não precisa declara explicitamente o tipo da variável que será utilizada no for como índice da execução.
            for letter in secret_word:
                if(guess == letter):
                    guessed_letters[index] = letter
                index += 1
        else:
            mistakes += 1
            print(f"You made {mistakes} mistakes.")

        if (mistakes >= 5):
            break

        got_it_right = "_" not in guessed_letters
        print(guessed_letters)

    if (got_it_right):
        print('You won!')
    else:
        print("You lost!")
