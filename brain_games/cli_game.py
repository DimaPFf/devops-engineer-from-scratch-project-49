from brain_games.constants import GAME_COUNT


def game_procces(game_cb, user_name):
    for i in range(GAME_COUNT):
        [answer, correct_answer] = game_cb()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")