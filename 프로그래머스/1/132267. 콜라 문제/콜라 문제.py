def solution(a, b, n):
    answer = 0
    
    while n >= a:  
        if n // a >= 1:
            # 교환 받은 콜라 수 갱신
            coke = (n // a) * b
            answer += coke # 개수 누적해서 답으로 저장
        
            # 나머지 값(교환 받지 못한 남은 병) + 교환 받은 병으로 보유중인 병 갱신
            n = (n % a) + coke
    
    return answer