from math import ceil
    
def solution(fees, records):
    answer = []
    parking = {}
    using_time = {}
    default_time, default_fee, unit_time, unit_fee = fees
    
    for record in records:
        time, number, history = record.split()
        hours, minutes = map(int, time.split(":"))

        time = (hours * 60) + minutes

        if history == "IN": # IN의 경우 time은 입차시간이 됨
            parking[number] = time
        elif history == "OUT": # OUT의 경우 time은 출차시간이 됨
            if number in using_time:
                using_time[number] += (time - parking[number]) # 출차시간 - 입차시간 누적
            else:
                # using_time이 기존에 존재하지 않는다면, 출차 시간 - 입차 시간을 초기 값으로 설정
                using_time[number] = time - parking[number]
            # 출차 처리
            del parking[number]
        
    LAST_TIME = (23 * 60) + 59  # 마지막 시각인 23:59을 분으로 변환

    for number, time in parking.items():
        if number in using_time:
            using_time[number] += (LAST_TIME - time)  # 남은 시간 누적
        else:
            using_time[number] = (LAST_TIME - time)  # 처음 계산되는 경우

    sorted_numbers = sorted(using_time.keys())  # 차량 번호만 정렬
    
    for number in sorted_numbers:
        time = using_time[number]
        extra_fee = max(0, ceil((time - default_time) / unit_time)) * unit_fee
        answer.append(default_fee + extra_fee)

    return answer