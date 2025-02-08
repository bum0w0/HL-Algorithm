def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]

    for baby in babbling:  
        for char in word:  
            if char * 2 not in baby:  # 연속된 단어가 없을 때만 변환 가능
                baby = baby.replace(char, ' ')  # 해당 단어를 공백으로 변환
        if baby.isspace():  # 모든 단어가 제거되어 공백만 남았을 경우
            answer += 1  # 정답 카운트 증가

    return answer