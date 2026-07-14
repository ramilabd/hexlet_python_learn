def run(text):
    # BEGIN (write your solution here)
    take_last = lambda text, n: text[-1:-5:-1] if text != '' and len(text) >= 4 else None
    # END
    return take_last(text, 4)


# print(run('cb'))
