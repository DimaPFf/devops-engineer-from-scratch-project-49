import random

import prompt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces

GAME_COUNT = 3


def game():
    num = random.randint(1, 100)
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return [answer, correct_answer]


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_procces(game, name)


if __name__ == '__main__':
    main()