def get_fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b



fib = get_fibonacci()

for x in fib:
    print(x)
    if x > 10:
        break