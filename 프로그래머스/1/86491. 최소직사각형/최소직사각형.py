def solution(sizes):
    width = []
    height =[]

    for i in sizes:
        width.append(max(i))
        height.append(min(i))

    print(width)
    print(height)

    return max(width) * max(height)