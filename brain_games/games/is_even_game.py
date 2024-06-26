import random


DESCRIPTION = ('Answer "yes" if the number is even, '
               'otherwise answer "no".')


def get_is_even_game():

    number = random.randint(1, 100)
    question = f"{number}"

    correct_answer = "yes" if number % 2 == 0 else "no"
    return correct_answer, question
