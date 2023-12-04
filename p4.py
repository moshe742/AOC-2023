def get_data():
    with open('p4_data.txt') as f:
        yield from f.readlines()


def parse_data():
    for line in get_data():
        if not line:
            continue
        line = line.strip()
        winning_numbers, available_numbers = line.split('|')
        card, winning_numbers = winning_numbers.split(':')
        *_, card_number = card.split(' ')
        card_number = card_number.strip()
        winning_numbers = [number.strip() for number in winning_numbers.split(' ') if number]
        available_numbers = [number.strip() for number in available_numbers.split(' ') if number]
        yield card_number, winning_numbers, available_numbers


def first():
    res = 0
    for card_num, win_numbers, available_numbers in parse_data():
        score = 0.5
        for num in available_numbers:
            if num in win_numbers:
                score *= 2
        if score > 0.5:
            res += int(score)
    return res


def second():
    data = list(parse_data())
    res = [1] * len(data)
    for idx, (card_num, win_numbers, available_numbers) in enumerate(data):
        count = 0
        for num in available_numbers:
            if num in win_numbers:
                count += 1
        for num in range(1, count + 1):
            res[idx + num] = res[idx] + res[idx + num]
    return sum(res)


if __name__ == '__main__':
    print(first())
    print(second())
