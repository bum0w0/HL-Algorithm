def solution(food):
    answer = ''

    player1 = []
    player2 = []

    for i in range(1, len(food)):
        if food[i] // 2 > 0:
            player1.extend([i] * (food[i] // 2))
        else:
            continue

    player2 = list(reversed(player1))

    answer = "".join(map(str, player1 + [0] + player2))

    return answer