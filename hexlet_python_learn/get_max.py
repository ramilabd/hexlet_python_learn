def get_max(numbers:list):
    if numbers == []:
        return None
        
    max, *tail = numbers

    for num in tail:
        if num > max:
            max = num

    return max


print(get_max([1, 10, 8]))
