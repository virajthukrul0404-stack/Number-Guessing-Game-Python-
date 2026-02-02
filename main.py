import random

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 10 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 10, 5
        elif choice == '2':
            return 50, 7
        elif choice == '3':
            return 100, 10
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    max_number, attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\nI have selected a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\n🎉 Congratulations! You guessed the number in {attempt} attempts.")
            return

    print(f"\n❌ Game Over! The correct number was {secret_number}.")

def main():
    print("🎯 Welcome to the Number Guessing Game!")

    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
