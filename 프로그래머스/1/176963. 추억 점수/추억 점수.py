def solution(name, yearning, photo):

    result = []
    ny_dict = dict(zip(name, yearning))

    for people in photo:

        total = 0

        for person_i_miss in people:
            total += ny_dict.get(person_i_miss, 0)
        result.append(total)

    return result