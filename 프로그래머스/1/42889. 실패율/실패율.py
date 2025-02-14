def solution(N, stages):
    answer = []
    failureRates = {}

    player_count = len(stages)

    for stage in range(1, N + 1):
        failed_players = stages.count(stage)
        
        if player_count != 0:
            failureRates[stage] = failed_players / player_count
        else:
            failureRates[stage] = 0  

        player_count -= failed_players

    sorted_failureRates = sorted(failureRates.items(), key=lambda x: x[1], reverse=True)

    for stage, _ in sorted_failureRates:
        answer.append(stage)

    return answer