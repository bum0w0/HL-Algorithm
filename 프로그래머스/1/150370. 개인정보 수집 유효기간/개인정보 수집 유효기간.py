def time_convert(time):
    Year, Month, Days = time.split('.')
    return (int(Year) * 12 * 28) + (int(Month) * 28) + int(Days)


def solution(today, terms, privacies):

    today = time_convert(today)

    terms_dict = {}
    
    for term in terms:
        term, Month = term.split()
        terms_dict[term] = int(Month) * 28

    answer = []

    for idx, privacy in enumerate(privacies, 1):
        time, policy = privacy.split()
        expiration_date = time_convert(time) + terms_dict[policy]

        if today >= expiration_date:
            answer.append(idx)

    return answer