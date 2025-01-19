# 1. 문자열 s를 순회
# 1-1. 문자열과 인덱스가 모두 필요 -> enumerate 사용

# 2. 등장한 문자들의 마지막 위치를 저장할 자료구조 사용 (딕셔너리가 적합)
# 2-1. 현재 문자가 딕셔너리에 없다면, -1을 결과 리스트에 추가
# 2-2. 현재 문자가 딕셔너리에 있다면, 현재 인덱스와 저장된 마지막 인덱스의 차이를 계산하여 결과 리스트에 추가

# 3. 순회를 완료한 후 결과 리스트 반환

def solution(s):
    
    find_word = {}
    result = []

    for i, char in enumerate(s):
        if char in find_word:
            result.append(i - find_word[char])
        else:
            result.append(-1)
            
        find_word[char] = i

    return result