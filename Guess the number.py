print("Guess the number game!!! You have 7 guesses to guess a number between 0-50! GOOD LUCK!")
import random
rand_num = random.randint(1,50)
guess = int(input("enter a number between 1-50: "))
out_of_guesses = False
guess_count = 1
while rand_num != guess and out_of_guesses == False:
    if guess > 50:
        print("number exceeds 50")
        guess = int(input("enter a number between 1-50: "))
    if guess < rand_num:
        print("Guess higher:")
        guess = int(input("enter a number between 1-50: "))

    else:
        print("Guess lower: ")
        guess = int(input("enter a number between 1-50: "))

    guess_count += 1

    if guess_count == 7:
        out_of_guesses = True

if guess == rand_num:
    print("You guessed it correctly!!")

else:
    print("Out of guesses!")






