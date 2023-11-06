number_of_trials = 0
lucky_number = 9
while number_of_trials < 4:
    user_guess = int(input("Guess: "))
    if user_guess == lucky_number:
        print("You win!")
        break
    number_of_trials += 1
else:
    print("Sorry you failed!")