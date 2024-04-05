import random
hard_diff = 5
easy_diff = 10
turn_off = True


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == 'easy':
        return easy_diff
    else:
        return hard_diff


def check_answer(guess_number, number, turns):
    global turn_off
    if guess_number < number:
        print('Too low.')
        return turns - 1
    elif guess_number > number:
        print('Too high.')
        return turns - 1
    else:
        print(f'You got it! The answer was {number}.')
        turn_off = False


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    # print(number)
    turns = set_difficulty()
    global turn_off
    while turn_off:
        if turns != 0:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess_number = int(input('Make a guess: '))
            turns = check_answer(guess_number, number, turns)
        elif turns == 0:
            print('You lose')
            turn_off = False


game()
