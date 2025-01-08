def solution(keymap, targets):

    key_dict = {}

    for key in keymap:
        for i, char in enumerate(key):
            if char in key_dict:
                # 최소 횟수를 찾기 (이전 입력 횟수와 비교하고 필요한 경우 갱신)
                key_dict[char] = min(key_dict[char], i + 1)

            else:
                # 처음 등장한 경우 (key_dict에 알파벳이 존재하지 않는 경우 입력 횟수 저장..i는 인덱스니까 횟수를 구하려면 + 1 해서 저장하기)
                key_dict[char] = i + 1


    result = []
    for target in targets:
        total = 0
        for char in target:
            if char in key_dict:
                total += key_dict[char] 
            else:
                total = -1  # 입력 불가
                break
        result.append(total)

    return result