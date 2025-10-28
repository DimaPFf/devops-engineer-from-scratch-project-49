import prompt
import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_count = 0
    for i in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if answer == correct_answer:
            correct_answer_count += 1
            print('Correct!')
        elif answer == correct_answer:
            correct_answer_count += 1
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
    if correct_answer_count > 2: 
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")

if __name__ == '__main__':
    main()