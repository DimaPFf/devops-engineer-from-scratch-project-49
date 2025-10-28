import random

import prompt

from brain_games.cli import welcome_user

GAME_COUNT = 3


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_count = 0
    for i in range(GAME_COUNT):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if answer == correct_answer:
            correct_answer_count += 1
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()