def isOneEditAway(small_str, large_str):
    for ch in small_str:
        if ch not in large_str:
            return False
    return True


def isOneSubAway(str1, str2):
    first_sub = False
    for i in range(len(str1)):
        ch = str1[i]
        if ch != str2[i]:
            if not first_sub:
                first_sub = True
            else:
                return False
    return True


def isOneAway(str1, str2):
    if len(str1) + 1 == len(str2):
        # one insertion away
        return isOneEditAway(str1, str2)
    elif len(str2) + 1 == len(str1):
        # one delete away
        return isOneEditAway(str2, str1)
    elif len(str1) == len(str2):
        # one  substitution away
        return isOneSubAway(str1, str2)
    return False
