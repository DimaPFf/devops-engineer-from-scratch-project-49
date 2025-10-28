import random

import prompt

from math import isqrt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def game():
    number = random.randint(0, 1000)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ').strip()
    correct_answer =  "yes" if is_prime_number(number) else "no"
    return [answer, str(correct_answer)]


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_procces(game, name)


if __name__ == '__main__':
    main()