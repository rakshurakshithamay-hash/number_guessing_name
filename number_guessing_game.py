import random
def number_guessing_game():
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    user_input = input("Enter your guess number (1-100):").strip()
    if not user_input.isdigit():
       print("Please enter a valid whole number!")
       continue
    guess = int(user_input)
    attempts += 1
    if guess < 1 or guess > 100:
       print("Out of bounds! Please enter a number between 1 and 100.")
       continue
    if guess < secret_number:
       print("Too low! Try again.")
    elif guess > secret_number:
       print("Too High! try again.")
    else:
       print(f"\n 🎉Congratulations! You guessed the correct number{secret_number}!")
       print(f"It took you {attempt} attempts.")
       break
if __name__ == "__main__":
   number_guessing_game()
