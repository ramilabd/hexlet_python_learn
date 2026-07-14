def invert_case(string):
    # BEGIN (write your solution here)
    """Invert string

        >>> invert_case('')
        ''

        >>> invert_case('Hexlet')
        'hEXLET'

        >>> invert_case('hexlet')
        'HEXLET'
        """
    # END

    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    failed, attempted = doctest.testmod()
    assert failed == 0
    assert attempted == 3