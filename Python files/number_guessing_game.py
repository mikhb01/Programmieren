# Number Guessing Game in Python
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("--------------------------------------------------")
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")
print("--------------------------------------------------")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print("--------------------------------------------------")
            print(f"Please select a number between {lowest_num} and {highest_num}")
            print("--------------------------------------------------")
        elif guess < answer:
            print("--------------------------------------------------")
            print("Too low! Try again")
            print("--------------------------------------------------")
        elif guess > answer:
            print("--------------------------------------------------")
            print("Too high! Try again!")
            print("--------------------------------------------------")
        else: 
            print("--------------------------------------------------")
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            print("--------------------------------------------------")
            is_running = False
    else:
        print("--------------------------------------------------")
        print("Invalid guess")
        print("--------------------------------------------------")
        print(f"Please select a number between {lowest_num} and {highest_num}")
        print("--------------------------------------------------")
