# 1. 여러개의 테스트 케이스(모음) 입력받기
# 2. 테스트 케이스 순회
# 2-1. a, e, i, o, u 중 하나를 반드시 포함 (in 사용?)
# 2-2. 모음 혹은 자음이 3개 연속으로 오면 안됨
# 3. 같은 글자가 연속적으로 두 번 오면 안되지만 ee와 oo는 허용

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()

    if password == 'end':
        break

    is_acceptable = True
    has_vowel = False
    vowel_streak = 0
    consonant_streak = 0
    prev = ''


    for ch in password:
        if ch in vowels:
            has_vowel = True
            vowel_streak += 1
            consonant_streak = 0 # 자음 연속 추적 초기화
        else:
            consonant_streak += 1
            vowel_streak = 0 # 모음 연속 추적 초기화
        
        if vowel_streak == 3 or consonant_streak == 3:
            is_acceptable = False
            break

        if ch == prev and ch not in ('e', 'o'):
            is_acceptable = False
            break

        prev = ch

    if not has_vowel: # 모음이 없다면
        is_acceptable = False # not acceptable 처리

    if is_acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
