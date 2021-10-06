"""
file:       guessing_game.py
created:    9/27/2021 9:11 PM
author:     ciaran mcdevitt
version:    v1.0.0
licensing:  (c) 2021 Ciaran McDevitt, LYIT
            available under the GNU Public License (GPL)
description:
credits:

"""
import random   # >> random to generate a random int
import time     # >> time to add waits for the flow of the gameplay

if __name__ == '__main__':
    '''
    main function for a guessing game where a user tries to guess a randomly generated number
     between one of three ranges selected from the menu  

    Parameters:
    argument1 (int): lower_range (lowest number of guessing range)
    argument2 (int): upper_range (highest number of guessing range, dynamically set through the menu)
    argument3 (int): guess_counter (keeps track of the number of guesses, displayed in output)
    argument4 (str): chosen_number (for user to select a difficulty level, then cast to an int once checked - isdigit())
    argument5 (str): option (for user to select a difficulty level in menu, 1, 2 or 3 to proceed, any other key to quit)
    argument6 (int): number_to_guess (initialized to zero and then set by difficulty level in menu)
    argument7 (bool): happy_to_keep_playing (initialized to true, could be used to return to menu instead of quitting) 
    argument8 (str): had_enough (after each guess users are asked if they wish to continue or to exit the game)  
    
    Output:
    Users are informed whether their guess is too low, to high or when the guess correctly are informed
     of how many guesses it took
    Each time a user make a guess, if unsuccessful the user is asked if they wish to continue playing
    '''

    lower_range = 1
    upper_range = 0
    guess_counter = 0
    chosen_number = 0
    option = 1
    number_to_guess = 0
    happy_to_keep_playing = True

    while option:
        print("\n______________________________________________\n"
              "Guessing Game Menu\n"
              "______________________________________________\n\n"
              "Select difficulty level of new game\n\n"
              "(1)  -Level 1  [1 - 100]\n"
              "(2)  -Level 2  [1 - 1000]\n"
              "(3)  -Level 3  [1 - 10000]\n\n"
              "-Press any other key to exit the game\n\n"
              " ~ Please enter a choice: ~\n\n\n\t")

        option = input()

        if option == '1':
            print("New game at Level 1!\n")
            upper_range = 100
            number_to_guess = random.randint(lower_range, upper_range)
            # print(f"number_to_guess: {number_to_guess}")  # print out number_to_guess so plural grammar can be tested
        elif option == '2':
            print("New game at Level 2!\n")
            upper_range = 1000
            number_to_guess = random.randint(lower_range, upper_range)
        elif option == '3':
            print("New game at Level 3!\n")
            upper_range = 10000
            number_to_guess = random.randint(lower_range, upper_range)
        # ********************************************************************************
        # Test: to confirm that range can be met but not breached (uncomment to activate)
        # ********************************************************************************
        # elif option == "RANGE-TEST":
        #     upper_range = 10000
        #     number_to_guess = random.randint(lower_range, upper_range)
        #     for i in range(1000000):
        #         number_to_guess = random.randint(lower_range, upper_range)
        #         if number_to_guess > 10000:
        #             print("fail")
        #             print(f"number_to_guess: {number_to_guess}")
        #             time.sleep(5)
        #         elif number_to_guess == 10000:
        #             print(f"#{i}/1000000 : 10000")
        #             time.sleep(5)
        #         else:
        #             pass
        # ********************************************************************************
        else:
            print("Goodbye")
            time.sleep(2)
            quit()

        while happy_to_keep_playing:
            guess_counter += 1
            if guess_counter == 1:
                correct_grammar = "a"
            else:
                correct_grammar = "another"

            chosen_number = input(f"Please enter {correct_grammar} number "
                                  f"between {lower_range} and {upper_range}\n  ")

            if chosen_number.isdigit():
                chosen_number = int(chosen_number)
            else:
                print("That's not an int... ")

            if lower_range <= chosen_number < upper_range:
                if chosen_number == number_to_guess:
                    if guess_counter == 1:
                        plural_or_not = "guess"
                    else:
                        plural_or_not = "guesses"
                    print(f"Congratulations! {chosen_number} is correct\n"
                          f" It took you {guess_counter} {plural_or_not}.  Well done!")
                    time.sleep(5)
                    break
                elif chosen_number > number_to_guess:
                    print("You've guessed to high...\n")
                else:
                    print("You've guessed to low...\n")

                had_enough = input("Keep playing?\t( n / any other key )\n")
                if had_enough == 'n' or had_enough == 'N':
                    # happy_to_keep_playing = False
                    confirmation_check = input("Are you sure you want to quit ( y / any other key)\n")
                    if confirmation_check == "y" or confirmation_check == "Y":
                        print("Goodbye")
                        time.sleep(2)
                        quit()

            else:
                print("Be careful not to waste attempts guessing out of range")


