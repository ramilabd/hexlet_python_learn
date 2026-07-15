from math import sqrt

def smallest_divisor_ver_1(n):
    if n == 1:
        return 1

    def inner (n, divisor):
        if divisor > n // 2:
            return n
        elif n % divisor == 0:
            return divisor
        return inner(n, divisor + 1)

    return inner(n, 2)


def smallest_divisor_ver_2(n):
       if n == 1:
           return 1

       def inner(divisor):
           if divisor > n // 2:
               return n
           if n % divisor == 0:
               return divisor
           return inner(divisor + 1)

       return inner(2)

def smallest_divisor_ver_3(n):
       if n == 1:
           return 1

       def inner(divisor):
           if divisor > sqrt(n):
               return n
           if n % divisor == 0:
               return divisor
           return inner(divisor + 1)

       return inner(2)

print(smallest_divisor_ver_1(25))
print(smallest_divisor_ver_2(25))
print(smallest_divisor_ver_3(25))
