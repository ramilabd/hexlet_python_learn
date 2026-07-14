from itertools import chain


def get_girl_friends(users):
    def extract_friends(user):
        return user.get('friends', [])

    def is_female(friend):
        return friend.get('gender', []) == 'female'

    extracted_friends = map(extract_friends, users)
    extracted_female = filter(is_female, list(chain.from_iterable(extracted_friends)))

    return list(extracted_female)

users = [
    {
        'name': 'Tirion',
        'friends': [
            {'name': 'Mira', 'gender': 'female'},
            {'name': 'Ramsey', 'gender': 'male'},
        ],
    },
    {'name': 'Bronn', 'friends': []},
    {
        'name': 'Sam',
        'friends': [
            {'name': 'Aria', 'gender': 'female'},
            {'name': 'Keit', 'gender': 'female'},
        ],
    },
    {
        'name': 'Rob',
        'friends': [
            {'name': 'Taywin', 'gender': 'male'},
        ],
    },
]

print(get_girl_friends(users))
# => [
# =>     {'name': 'Mira', 'gender': 'female'},
# =>     {'name': 'Aria', 'gender': 'female'},
# =>     {'name': 'Keit', 'gender': 'female'},
# => ]
