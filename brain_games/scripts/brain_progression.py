import random

import prompt

from brain_games.cli import welcome_user
from brain_games.cli_game import game_procces
from brain_games.constants import (
    MAX_LENGT_PROGRESSIVE,
    MAX_NUMBER,
    MAX_STEP,
    MIN_LENGT_PROGRESSIVE,
    MIN_NUMBER,
    MIN_STEP,
)


def make_progression():
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    length = random.randint(MIN_LENGT_PROGRESSIVE, MAX_LENGT_PROGRESSIVE)
    step = random.randint(MIN_STEP, MAX_STEP)
    nums = []
    for i in range(length):
        num = start + i * step 
        nums.append(num)
    return nums


def game():
    progression = make_progression()
    correct_answer_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_index]
    progression[correct_answer_index] = '..'
    print_progression = ' '.join(map(str, progression))
    print(f'Question: {print_progression}')
    answer = prompt.string('Your answer: ').strip()
    return [answer, str(correct_answer)]


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    game_procces(game, name)


if __name__ == '__main__':
    main()