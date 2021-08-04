    print("\n****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    secret_word = "Apple".upper()
   
    guessed_letters = ["_" for letter in secret_word]

    hanged = False
    got_it_right = False
    mistakes = 0

    while(not hanged and not got_it_right):
        guess = input("\nWhich Letter? ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
          
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
