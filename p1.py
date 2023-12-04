def get_data():
    with open('p1_data.txt') as f:
        yield from f.readlines()


def find_start_end_digits(line):
    start = 0
    end = len(line) - 1
    while not line[start].isdigit():
        start += 1
    while not line[end].isdigit():
        end -= 1
    return start, end


def first():
    numbers = []
    for line in get_data():
        start, end = find_start_end_digits(line)
        numbers.append(int(f'{line[start]}{line[end]}'))
    return sum(numbers)


def second():
    text_numbers = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    res = []
    for line in get_data():
        start = len(line)
        end = -1

        for num in text_numbers.keys():
            found = line.find(num)
            if -1 < found < start:
                start = line.find(num)
                possible_start = text_numbers[num]
            r_found = line.rfind(num)
            if -1 < r_found and end < r_found:
                end = r_found
                possible_end = text_numbers[num]

        try:
            pos_start, pos_end = find_start_end_digits(line)
        except IndexError:
            start = possible_start
            end = possible_end
            res.append(int(f'{start}{end}'))
            continue

        if pos_start < start:
            start = line[pos_start]
        else:
            start = possible_start

        if pos_end > end:
            end = line[pos_end]
        else:
            end = possible_end

        res.append(int(f'{start}{end}'))
    return sum(res)


if __name__ == '__main__':
    print(first())
    print(second())
