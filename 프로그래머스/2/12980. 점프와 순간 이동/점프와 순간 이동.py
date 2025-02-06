def solution(n):
    battery_usage = 0

    while n > 0:
        # 순간이동 가능하면
        if n % 2 == 0:
            # 순간 이동 하기
            n = n // 2
        # 순간이동 못하면
        else:
            # 1칸 이동한걸로 치고 건전지 사용량 += 1
            n -= 1
            battery_usage += 1

    return battery_usage