import random

import prompt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces
from brain_games.constants import EVEN_NUMBER, MAX_NUMBER, MIN_NUMBER


def game():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    correct_answer = 'yes' if num % EVEN_NUMBER == 0 else 'no'
    return [answer, correct_answer]


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_procces(game, name)


if __name__ == '__main__':
    main()