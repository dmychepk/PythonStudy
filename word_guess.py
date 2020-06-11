import random

class Game():

    def __init__(self, *, number_of_erros):
        self.number_of_erros = number_of_erros
        self.word = ''
        self.named_letters = []
        self.user_word = []

    def generate_word(self):
        with open('original.txt') as word_file:
            self.word = random.choice(word_file.readlines()).strip()
            print(self.word)

    def guess_letter(self, letter):
        self.named_letters.append(letter)
        self.user_word = []

        for i,k in enumerate(self.word):
            if k not in self.named_letters:
                self.user_word.append('*')
            else:
                self.user_word.append(k)
        if ''.join((self.user_word)) == self.word:
            return True

        if letter in self.word:
            print(f'You guessed! Letter "{letter}" is in word.')
        else:
            print(f'You didn\'t guess! Letter "{letter}" is not in word.')
            self.number_of_erros -= 1

    def print_word(self):
        return ''.join((self.user_word))

    def opened_letters(self):
        return sorted(self.named_letters)



my_game = Game(number_of_erros=15)
my_game.generate_word()

while my_game.number_of_erros > 0:
    print(f'You have {my_game.number_of_erros} attempts left')
    player_guess = input('Enter your word: ')

    if not my_game.guess_letter(player_guess):

        print(f'Currently the word is {my_game.print_word()}')
        print(f'You opened letters {my_game.opened_letters()}')
    else:
        print(f'You win! Word is {my_game.print_word()}')
        break

if my_game.number_of_erros == 0:
    print('You lost!')





