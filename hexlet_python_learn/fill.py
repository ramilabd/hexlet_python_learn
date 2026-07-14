def fill(coll, value, begin=None, end=None):
    if begin is None and end is None:
        return [value] * len(coll)
    elif (not begin is None and begin >= len(coll)):
        return coll
    elif (not begin is None and begin < len(coll) and end is None):
        end = len(coll)
        for i in range(begin, end):
            coll[i] = value
        return coll
    elif not begin is None and not end is None:
        if end >= len(coll):
            end = len(coll)
            for i in range(begin, end):
                coll[i] = value
            return coll
        else:
            for i in range(begin, end):
                coll[i] = value
            return coll


def fill(coll, value, begin=0, end=None):
    if end is None:
        end = len(coll)
    # Ограничиваем end длиной списка, чтобы не выйти за границы
    end = min(end, len(coll))
    # Если begin за пределами или диапазон пуст — ничего не делаем
    if begin >= len(coll) or begin >= end:
        return
    for i in range(begin, end):
        coll[i] = value

coll =  [1, 2, 3, 4]

print(fill(coll, '*') == ['*', '*', '*', '*'])
print(fill(coll, '*', 4) == [1, 2, 3, 4])
print(fill(coll, '*', 2) == [1, 2, '*', '*'])
print(fill(coll, '*', 0, 10) == ['*', '*', '*', '*'])
print(fill(coll, '*', 1, 3) == [1, '*', '*', 4])