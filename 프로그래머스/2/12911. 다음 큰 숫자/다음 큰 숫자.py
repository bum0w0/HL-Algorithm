def solution(n):
    origin_count = bin(n).count("1")  

    while True:
        n += 1  
        if bin(n).count("1") == origin_count:
            return n  