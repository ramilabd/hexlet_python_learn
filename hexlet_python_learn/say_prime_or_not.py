from math import sqrt


def is_prime(num: int):
    divider = 2
    max_div = sqrt(num)

    while divider <= max_div:
        if num % divider == 0:
            return False
        divider += 1

    return True
    

def say_prime_or_not(num: int):
    answer = 'yes' if is_prime(num) else'no'
    print(answer)


say_prime_or_not(3)