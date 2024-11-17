def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    lux, luy = n, m
    rdx, rdy = 0, 0

    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    
    print(f"시작점 : {lux}, {luy}")
    print(f"끝점 : {rdx}, {rdy}")

    # 드래그 시작점 (lux, luy)와 끝점 (rdx, rdy)는 lux < rdx, luy < rdy를 만족해야 함.
    


    result = [lux, luy, rdx + 1, rdy + 1]

    return result