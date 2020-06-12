import true_or_false_server as game

my_game = game.Game('original.csv', 2)
my_game.start_the_game()

while my_game.game_status == 'In progress':

    print(f'The question is: {my_game.next_question()}')
    answer = input('Enter your answer [y/n]:')

    correct_answer, explanaition = my_game.correct_answer(answer)
    if correct_answer is True:
        print(f'You answer is correct - {explanaition}')
    else:
        print(f'You answer is wrong - {explanaition}')

if my_game.game_status == 'WIN':
    print('You are winner!')
if my_game.game_status == 'LOST':
    print('You are looser!')




