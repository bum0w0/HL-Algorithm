def solution(ingredient):
    count = 0

    pattern = [1, 2, 3, 1]
    p_len = len(pattern)

    i = 0
    while i <= len(ingredient) - p_len:
        if ingredient[i:i+p_len] == pattern:
            del ingredient[i:i + p_len]  # 패턴을 제거
            count += 1
            i = max(0, i - p_len + 1)
        else:
            i += 1

    return count