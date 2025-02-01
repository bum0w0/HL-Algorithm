def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)

    number = list(zip(A, B))
    for num in number:
        print(num)
        answer += num[0] * num[1]
        


    return answer