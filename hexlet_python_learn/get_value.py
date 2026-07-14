table = [
    None,
    ("e", "foo"),
    ("f", "baz"),
    ("g", "bar"),
    None
]


def get_hash(key):
    return ord(key) % 5


def get_value(table, key):
    index = get_hash(key)
    data = table[index]
    
    if data is None:
        return "not found"
    
    found_key, found_value = data
    if found_key != key:
        return "collision"
    return found_value
    

print(get_value(table, 'l'))
