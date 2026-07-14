def id_generator(pref: str):
    id = 0

    def id_gen():
        nonlocal id
        id += 1
        return f'{pref}-{id:03d}'
    
    return id_gen


user_id = id_generator("USER")
print(user_id())  # => "USER-001"
print(user_id())  # => "USER-002"
print(user_id())  # => "USER-003"
