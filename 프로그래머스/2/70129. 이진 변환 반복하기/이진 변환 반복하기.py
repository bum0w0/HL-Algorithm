def solution(s):
    zero = 0
    count = 0

    while s != "1":
        # 110010101001
        zero += s.count("0")
        s = s.replace("0", "")
        # 111111
        c = len(s) # c = 6
        s = bin(c)[2:] # 110
        count += 1
    return [count, zero]
