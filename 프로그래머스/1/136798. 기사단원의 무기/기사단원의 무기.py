import math

# 약수 개수 구하는 로직
def divisor(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1  # 작은 약수
            if i != n // i:  # 큰 약수 (중복 방지)
                count += 1
    return count

def solution(number, limit, power):

    div_count = list(map(divisor, range(1, number + 1)))

    s_num = 0

    for count in div_count:
        if count > limit:
            s_num += power
        else:
            s_num += count

    return s_num
