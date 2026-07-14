def get_average(*numbers):
    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)


print(get_average(0)) # 0
print(get_average(0, 10)) # 5
print(get_average(-3, 4, 2, 10)) # 3.25
print(get_average()) # None