# 1. 투포인터?
# 2. 일단 p의 길이가 주어짐. 그럼 투 포인터 옮겨갈 때 최대 길이가 3
# 3. t의 길이가 p인 부분 문자열을 찾고, p 보다 작거나 같은수 return

def solution(t, p):


    p_len = len(p)
    left = 0
    right = p_len
    answer = 0
    
    while right <= len(t):
        substring = int(t[left:right]) # 부분 문자열 정의 (지금 예시에서는 0~3까지)

        if substring <= int(p): # 부분 문자열 (Ex. 314가 271보다 작으면 answer 증가, 근데? 안작음 그럼 포인터 옮겨줌)
            answer += 1
        
        # 포인터 옮겨가면 다음 비교해볼 수는 314 -> 141이 됨
        left += 1
        right += 1

    return answer

