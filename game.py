import random
import functions

while True:

    try:
        lower_range = int(input("\nLowest number? : "))
        upper_range = int(input("\nHighest number? : "))
    except ValueError:
        print("Choose a number")
        continue

    if lower_range >= upper_range:
        print("Lowest number must be less than the highest...\n")
        functions.pause()
        continue

    break

number = random.randint(lower_range, upper_range)

functions.clear()

guesses = 0

while True:
    try: 
        choice = int(input("\nWhat is your guess? : "))
    except ValueError:
        print("\nChoose a number!")
        continue

    if choice == number:
        print("\nCorrect!")
        guesses = guesses + 1 
        print("\nYou guessed", guesses, "Times!\n")
        functions.pause()
        break
    elif choice < number:
        print("\nHigher!")    
        guesses = guesses + 1   
    elif choice > number:
        print("\nLower!")
        guesses = guesses + 1