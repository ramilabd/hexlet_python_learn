def get(coll, index, default=None):

    if (index >= len(coll) or index < 0):
        if default is not None:
            return default
        return None

    return coll[index]

# print(get([2, 5, 6, 7, 8], 2))
print(get([1, 2, 3], 1, "a"))