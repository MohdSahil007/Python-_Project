#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of allowed attempts
    attempts_left = 5
    
    while attempts_left > 0:
        try:
            # Get the player's guess
            player_guess = int(input(f"Enter your guess (1-100). Attempts remaining {attempts_left}: "))
        
            # Check if the guess is correct
            if player_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                break
            # If the guess is too high or low, provide feedback
            elif player_guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            # Handle non-numeric input
            print("Please enter a valid number.")
            continue
        
        # Decrease the number of remaining attempts
        attempts_left -= 1
    
    # If the player runs out of attempts
    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}. Better luck next time!")

# Run the game
guess_the_number()


# In[ ]:




