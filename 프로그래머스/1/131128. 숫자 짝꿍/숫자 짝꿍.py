def solution(X, Y):
    count_x = [0] * 10  
    count_y = [0] * 10  

    # X와 Y에서 숫자 개수 세기
    for num in X:
        count_x[int(num)] += 1
    for num in Y:
        count_y[int(num)] += 1

    answer = ""

    for i in range(9, -1, -1):
        answer += str(i) * min(count_x[i], count_y[i])
    
    if not answer:
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer