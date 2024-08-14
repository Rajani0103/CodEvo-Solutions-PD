import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            
            if guess < number_to_guess:
                print("Try again!You guessed Too low!")
            elif guess > number_to_guess:
                print("Try again!You guessed Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess}.")
                return
            
            attempts -= 1
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"Better luck next time. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
