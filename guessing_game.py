"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random

# Create a list to hold the player's score history over multiple games
score_history = []

# Start game function runs all game code
def start_game():    
    
    # Display an intro/welcome message to the player.
    intro = '=========================================\nWelcome to the Number Guessing Game!\n========================================='
    print(intro)

    # Store a random number as the answer/solution. Make it generate a new number for every game.
    game_answer = random.randrange(1,10)
    
    # Initialize a boolean that will update to True when the user gets the right number
    is_correct_guess = False
    
    # Set a counter to track how many attempts there have been
    counter = 0
		
    # While user answer is not equal to game answer, keep asking them to try again
    while is_correct_guess == False:
        # Catch any exceptions from user input
        try:
            # Ask the user for a number
            user_answer = int(input("Pick a number between 1 and 10: "))
            # Increment the counter for each guess
            counter+=1
            
            # If user guesses outside of 1-10 range, remind them of the limit so they can try again.
            if user_answer not in range(1, 10):
                print("This is not a valid guess. The number is between 1 - 10. Please try again")
                # this shouldn't count against their score, so remove one point from counter
                counter-=1
            else:

                # If the user guesses incorrectly, give them a hint
                if user_answer != game_answer:
                    # If the guess greater than the solution, display to the player "It's lower".
                    if user_answer > game_answer:
                        print("It's lower")
                    # If the guess is less than the solution, display to the player "It's higher".
                    elif user_answer < game_answer:
                        print("It's higher")   
                # If the user guesses correctly, set boolean to True in order to break out of loop.                
                else:
                    is_correct_guess = True
                    # Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
                    print(f"Got it! It only took you {counter} attempts.")
                    # Append the total number of attempts to the score history
                    score_history.append(counter)
                    # Pick the lowest value in score_history (it will be player's best score)
                    best_score = min(score_history)
                    # Let the player know the game is ending, and display their high score
                    play_again = input(f"This game is over. Would you like to play again, and try to beat your best score of {best_score}? (Y/N)").lower()

                    # If user doesn't want to play again, say goodbye
                    if play_again == "n":
                        print("Thanks for playing! See you next time.")
                    # Otherwise, start another game
                    elif play_again =="y":    
                        start_game()
                    # If the user puts in a number or letter that doesn't apply, close the game.
                    else:
                        print("Sorry, we didn't recognize that answer and need to end the game.")
                            
        # If user input is invalid, give them an error.
        except ValueError as e:
            print(f"Your selection generated the following error: '{e}'. Please try again.")
                    
# Kick off the program by calling the start_game function.
start_game()