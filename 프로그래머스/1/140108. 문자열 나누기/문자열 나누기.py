def solution(s):
    answer = 0
    fw = 0 # 첫 문자 개수 추적
    dw = 0 # 다른 문자 개수 추적
    cw = ""

    for word in s:
        if fw == dw:
            answer += 1
            cw = word
        if cw == word:
            fw +=1
        else:
            dw +=1

    return answer