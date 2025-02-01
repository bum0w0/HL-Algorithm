def solution(s):
    
    number = list(map(int, s.split()))
    
    return f"{min(number)} {max(number)}"