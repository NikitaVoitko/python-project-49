import random

IS_PRIME_DESCRIPTION = ('Answer "yes" if given number is prime. '
                        'Otherwise answer "no".')


def is_prime(n):
    is_prime = "yes"
    if n <= 1:
        is_prime = "no"
    elif n <= 3:
        is_prime = "yes"
    elif n % 2 == 0 or n % 3 == 0:
        is_prime = "no"
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = "no"
    return is_prime


def is_prime_game():
    number = random.randint(1, 100)
    correct_answer = is_prime(number)
    question = f"{number}"
    return correct_answer, question
