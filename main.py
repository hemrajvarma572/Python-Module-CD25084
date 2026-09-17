import random

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)

# Generate random number
secret_number = random.randint(1, 100)

# Game settings
max_attempts = 10
attempts = 0

print("\nI have selected a number between 1 and 100.")
print("You have 10 attempts to guess it.")

while attempts < max_attempts:

    try:
        guess = int(input("\nEnter your guess: "))

        # Check range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too Low!")

        elif guess > secret_number:
            print("Too High!")

        else:
            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print("Number:", secret_number)
            print("Attempts used:", attempts)
            break

        # Show remaining attempts
        remaining = max_attempts - attempts
        print("Attempts remaining:", remaining)

    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    print("\n❌ Game Over!")
    print("You used all 10 attempts.")
    print("The correct number was:", secret_number)

print("\nThank you for playing!")