#!/usr/bin/python3
def guess_game(x, y):
    magic_number = x
    no_of_attempts_made = 0
    no_of_attempts_left = y
    while no_of_attempts_left > no_of_attempts_made:
        no_of_attempts_left -= 1
        guess = int(input("guess the number : "))
        if guess == magic_number:
            print("correct")
            break
        else:
            print(f'try again, you have {no_of_attempts_left} attempts left')
    else:
        print('failed')


guess_game(3, 3)
