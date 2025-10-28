import random

import prompt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces
from brain_games.constants import MAX_NUMBER, MIN_NUMBER


def calc(num_1, num_2, op):
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2


def game():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    op = random.choice(['-', '+', '*'])
    print(f'Question: {num_1} {op} {num_2}')
    answer = prompt.string('Your answer: ').strip()
    correct_answer = calc(num_1, num_2, op)
    return [answer, str(correct_answer)]


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    game_procces(game, name)


if __name__ == '__main__':
    main()