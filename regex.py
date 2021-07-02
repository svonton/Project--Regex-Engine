def check(regex, string):
    return regex == '' or string != '' and (regex == string or regex == '.')


def recursive_matching(regex, string):
    if len(regex) == 0:
        return True
    if len(string) == 0:
        return False
    if check(regex[0], string[0]):
        return recursive_matching(regex[1:], string[1:])
    else:
        return False


def match(regex, string):
    if recursive_matching(regex, string):
        return True
    elif len(regex) < len(string):
        return match(regex, string[1:])
    else:
        return False


def start_end_check(regex, string):
    if regex != '' and regex[0] == '^':
        regex = regex[1:]
        if regex[0] != '.' and regex[0] != string[0]:
            return False
        if regex[-1] == '$':
            regex = regex[:-1]
            if regex != string:
                return False
        return match(regex, string)
    elif regex != '' and regex[-1] == '$':
        regex = regex[:-1]
        if len(regex) == 0:
            return False
        if regex[-1] != '.' and regex[-1] != string[-1]:
            return False
        return match(regex, string)
    else:
        return match(regex, string)


def multipl_char_check(regex, string):
    if '?' in regex:
        if start_end_check(regex.split(sep='?')[0], string):
            return start_end_check(regex.split(sep='?')[0]+(regex.split(sep='?')[1]), string)
        else:
            return start_end_check(regex.split(sep='?')[1], string)
    if '*' in regex:
        if start_end_check(regex.split(sep='*')[0], string):
            return start_end_check(regex.split(sep='*')[1], string)
        else:
            return start_end_check(regex.split(sep='*')[1], string)
    if '+' in regex:
        if start_end_check(regex.split(sep='+')[0], string) and len(regex) > len(string):
            return start_end_check(regex.split(sep='+')[0] + (regex.split(sep='+')[1]), string)
        elif start_end_check(regex.split(sep='+')[0], string):
            return start_end_check(regex.split(sep='+')[1], string)
        else:
            return False
    else:
        return start_end_check(regex, string)


def backslash(regex, string):
    if '\\' in regex:
        return start_end_check(regex.replace('\\', ''), string)
    else:
        return multipl_char_check(regex, string)


regex, string = input().split(sep='|')
print(backslash(regex, string))
