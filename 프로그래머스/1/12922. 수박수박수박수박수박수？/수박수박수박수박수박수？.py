n = 3

def solution(n):
    
    answer = ''
    fw = "수"
    sw = "박"
    

    for i in range(n):
        if i%2==0:
            answer += fw
        else:
            answer += sw

    return answer

print(solution(n))