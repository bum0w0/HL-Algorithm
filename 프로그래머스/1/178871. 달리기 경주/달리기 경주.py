players = ["mumu", "soe", "poe", "kai", "mine"]



def solution(players, callings):
    # player가 딕셔너리의 키가 되고, index가 값이 된다.
    # enumerate(players)는 players 리스트의 각 요소를 (순서, 값) 형태로 반환. Ex. (0, 'mumu')
    player_to_index = {player: index for index, player in enumerate(players)}

    for calling in callings:
        # 추월하는 선수의 순위 (이후에 위치를 바꿔줘야 하니 순위를 current_index에 저장해두기)
        current_index = player_to_index[calling]

        # 해설진이 이름을 불렀다면
        if current_index > 0:
            # 추월 당하는 바로 전 선수의 이름
            previous_player = players[current_index - 1]

            # 추월 당한 상황 (선수들 위치 바꾸기)
            players[current_index], players[current_index - 1] = players[current_index - 1], players[current_index]

            # 딕셔너리의 순위 값 갱신 (선두 주자는 -1 해서 순위를 낮추고, 추월 한 선수는 +1 하여 순위를 높임)
            player_to_index[calling] -= 1
            player_to_index[previous_player] += 1

    return players


