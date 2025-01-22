def solution(n, arr1, arr2):

    row_1, row_2 = [], []
    result = []

    for i in range(n):
        row_1.append(bin(arr1[i])[2:].zfill(n))
        row_2.append(bin(arr2[i])[2:].zfill(n))

    for i in range(n):
        union_row = ""
        for j in range(n):
            # 01001이랑 11110 합집합 만들기 (11110)
            if row_1[i][j] == '1' or row_2[i][j] == '1':
                union_row += '#'
            else:
                union_row += ' '
        result.append(union_row)

    return result