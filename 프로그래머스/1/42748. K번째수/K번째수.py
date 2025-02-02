def solution(array, commands):

    answer = 0
    result = []

    for command in commands:
        start, end, idx = command
        sorted_array = sorted(array[start-1:end])
        result.append(sorted_array[idx-1])
    
    return result