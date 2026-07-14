from functools import reduce

def group_by(coll, property):

    def group_by_property(acc, item):
        if item[property] not in acc:
            acc[item[property]] = []
        acc[item[property]].append(item)

        return acc

    return reduce(group_by_property, coll, {})



students = [
    {'name': 'Tirion', 'class': 'B', 'mark': 3},
    {'name': 'Keit', 'class': 'A', 'mark': 3},
    {'name': 'Ramsey', 'class': 'A', 'mark': 4},
]

print(group_by([], ''))  # => {}
print(group_by(students, 'mark'))

# => {
# =>   3: [
# =>     {'name': 'Tirion', 'class': 'B', 'mark': 3},
# =>     {'name': 'Keit', 'class': 'A', 'mark': 3},
# =>   ],
# =>   4: [
# =>     {'name': 'Ramsey', 'class': 'A', 'mark': 4},
# =>   ],
# => }