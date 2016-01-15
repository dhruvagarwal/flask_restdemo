def null_view(self, *args, **kwargs):
    return {}

def match(pattern, string):
    """String matching function with wildcard characters.
    """
    if not len(pattern) and not len(string):
        return True

    if len(pattern) > 1 and pattern[0] == '*' and len(string) == 0:
        return False

    if (len(pattern) > 0 and pattern[0] == '?') or \
        (len(pattern) != 0 and len(string) != 0 and pattern[0] == string[0]):
        return match(pattern[1:], string[1:])

    if len(pattern) != 0 and pattern[0] == '*':
        return match(pattern[1:], string) or match(pattern, string[1:])

    return False


def ismatch(pattern, args):
    # :param pattern: a tuple containing what to match
    # :param args: method arguments passed.

    pattern = map(str, pattern)
    args = map(str, args)

    if len(pattern) != len(args):
        return False

    for i in range(len(args)):
        # TODO: improve matching methods
        if not match(pattern[i], args[i]):
            return False

    return True

