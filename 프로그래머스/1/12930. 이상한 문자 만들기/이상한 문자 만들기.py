def solution(s):
    # 문자열을 공백 기준으로 나눔
    list_s = s.split(' ')
    result = []
    # 각 단어를 처리
    for i in list_s:
        answer = ''
        for j in range(len(i)):
            # 짝수 인덱스는 대문자로, 홀수 인덱스는 소문자로
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        # 결과 리스트에 추가
        result.append(answer)
    
    # 단어를 공백으로 연결하여 반환
    return ' '.join(result)