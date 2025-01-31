import string

def solution(s, n):
    alphabet1 = [char for char in string.ascii_lowercase]
    alphabet2 = [char for char in string.ascii_uppercase]
    
    result = []

    for char in s:
        if char == " ":
            result.append(" ")
            continue

        if char in alphabet1:
            new_index = (alphabet1.index(char) + n) % len(alphabet1)
            result.append(alphabet1[new_index])
        elif char in alphabet2:
            new_index = (alphabet2.index(char) + n) % len(alphabet2)
            result.append(alphabet2[new_index])

    return "".join(result)