#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "interface"]
    return random.choice(words)
class Hangman:
    def __init__(self):
        self.word = get_random_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def display_game_state(self):
        displayed_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(f"Current word: {displayed_word}")
        print(f"Incorrect guesses remaining: {self.max_attempts - self.incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed that letter.")
            return False
        
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.incorrect_guesses += 1
            print(f"Incorrect guess: {letter}")
            return False
        else:
            print(f"Correct guess: {letter}")
            return True

    def is_won(self):
        return set(self.word) <= self.guessed_letters

    def is_lost(self):
        return self.incorrect_guesses >= self.max_attempts

def main():
    game = Hangman()
    
    while not game.is_won() and not game.is_lost():
        game.display_game_state()
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        game.make_guess(guess)

    if game.is_won():
        print(f"Congratulations! You've guessed the word: {game.word}")
    else:
        print(f"Game over! The word was: {game.word}")

if __name__ == "__main__":
    main()


# In[ ]:




