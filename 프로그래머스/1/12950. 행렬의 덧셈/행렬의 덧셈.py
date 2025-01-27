def solution(arr1, arr2):

    answer = []

    for row1, row2 in zip(arr1, arr2):
        sum_row = []
        for i in range(len(row1)):
            sum_row.append(row1[i] + row2[i])
        answer.append(sum_row)
    
    return answer