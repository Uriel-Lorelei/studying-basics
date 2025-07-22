import random
secret_number = random.randint(1,20)
print("Guess between 1 to 20.")

for guesses_taken in range(1,7):
    print("Guess")
    guess = int(input(">"))
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break

if guess == secret_number:
    print(f"Good job. You got it in {guesses_taken} tries.")
else:
    print(f"Nope the number was {secret_number}.")