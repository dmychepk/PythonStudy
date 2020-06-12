import csv

class Game:

    def __init__(self, file: str, number_of_errors: int):
        self.file = file
        self.number_of_errors = number_of_errors

        self.__question_number = - 1
        self.__game_status = 'Not Started'
        self.__data = []
        self.__question = ''
        self.__wrong_answers = 0

    @property
    def game_status(self):
        return self.__game_status

    def start_the_game(self):
        self.read_file()
        self.__game_status = 'In progress'

    def read_file(self):
        my_file = open(self.file)
        data = csv.reader(my_file, delimiter=';')
        for line in data:
            self.__data.append(line)
        return self.__data

    def next_question(self):
        self.__question_number += 1
        if self.__question_number <= len(self.__data):
            if self.__game_status == 'In progress':
                for i, row in enumerate(self.__data):
                    if i  == self.__question_number:
                        self.__question = row[0]
                        return self.__question


    def correct_answer(self, user_answer):
        for i, row in enumerate(self.__data):
            if i  == self.__question_number:

                if self.__question_number == len(self.__data) - 1:
                    self.__game_status = 'WIN'

                if row[1][0].lower() == user_answer:
                    return True, row[2]
                else:
                    self.__wrong_answers += 1
                    if self.__wrong_answers == self.number_of_errors:
                        self.__game_status = 'LOST'
                    return False, row[2]




