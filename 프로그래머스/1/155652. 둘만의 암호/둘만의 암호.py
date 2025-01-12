import string

def solution(s, skip, index):
    # 1. 사용할 수 있는 알파벳 리스트를 생성 (skip에 포함된 문자는 제외)
    alphabet = [char for char in string.ascii_lowercase if char not in skip]

    result = ""
    # 2. 주어진 문자열 s 순회
    for char in s:
        # 2-1. 현재 문자의 알파벳 리스트 내 인덱스 찾기
        current_index = alphabet.index(char)
        # 2-2. index만큼 이동 후, 리스트의 끝을 넘으면 처음부터 시작 (원형 처리)
        new_index = (current_index + index) % len(alphabet)
        # 2-3. 이동한 인덱스에 해당하는 문자를 결과에 추가
        result += alphabet[new_index]

    return result