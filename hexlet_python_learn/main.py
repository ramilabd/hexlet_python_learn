opening_symbols = ['(', '[', '{', '<']
closing_symbols = [')', ']', '}', '>']

def are_symbols_balanced(expression: str) -> bool:
    stack = []

    for ch in expression:
        if ch in opening_symbols:
            stack.append(ch)
        elif ch in closing_symbols:
            if not stack:
                return False
            
            close_idx = closing_symbols.index(ch)
            last_open = stack.pop()
            open_idx = opening_symbols.index(last_open)

            if open_idx != close_idx:
                return False

    return not stack


print(are_symbols_balanced('(>'));  # False
print(are_symbols_balanced('()'));  # True
print(are_symbols_balanced('[()]'));  # True
print(are_symbols_balanced('({}[])'));  # True
print(are_symbols_balanced('{<>}}')); # False
print(are_symbols_balanced('([)]')); # False
