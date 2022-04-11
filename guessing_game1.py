import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number bewteen 1 and {x}: '))
        if guess < random_number:
            print('Srry, guess again. Number too low')
        elif guess > random_number:
            print('Srry, guess again. Number too high')
        
    print('You guessed right!')


guess(10)