import random

import prompt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces


def find_nod(num_1, num_2):
    if num_2 == 0:
        return num_1
    return find_nod(num_2, num_1 % num_2)


def game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    print(f'Question: {num_1} {num_2}')
    answer = prompt.string('Your answer: ').strip()
    correct_answer = find_nod(num_1, num_2)
    return [answer, str(correct_answer)]


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_procces(game, name)


if __name__ == '__main__':
    main()