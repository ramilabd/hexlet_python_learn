basic_info = ('Alice', 30)
additional_info = {'city': 'New York', 'job': 'Engineer', 'hobby': 'painting'}


def format_person_info(name, age, **kwargs):
    base = f"Name: {name}, Age: {age}"

    if kwargs:
        sorted_keys = sorted(kwargs.keys())
        additional = ", ".join(
            f"{key.capitalize()}: {kwargs[key]}" for key in sorted_keys
        )
        return f"{base}, {additional}"
    return base


result = format_person_info(*basic_info, **additional_info)
print(result) # => Name: Alice, Age: 30, City: New York, Hobby: painting, Job: Engineer