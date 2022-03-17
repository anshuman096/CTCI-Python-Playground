# Given a string write a function to check if it is a permutation of a palindrome

def checkPalindrome(input_str: str):
    input_str = input_str.replace(" ", "")
    s_dict = {}
    for ch in input_str:
        if ch not in s_dict:
            s_dict[ch] = 1
        else:
            s_dict[ch] += 1
    if len(input_str) % 2 == 0:
        for ch in s_dict:
            if s_dict[ch] % 2 == 1:
                return False
    else:
        first_odd_freq = False
        for ch in s_dict:
            if s_dict[ch] % 2 == 1:
                if not first_odd_freq:
                    first_odd_freq = True
                else:
                    return False
    return True
