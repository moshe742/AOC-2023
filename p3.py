def get_data():
    with open('p3_data.txt') as f:
        data = [line.strip() for line in f.readlines()]
        return data


def check_nearby_numbers(data, row, column):
    numbers = []
    positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for pos in positions:
        if 0 <= row + pos[0] < len(data) and \
                0 <= column + pos[1] < len(data[0]) and \
                data[row + pos[0]][column + pos[1]].isdigit():
            numbers.append((row + pos[0], column + pos[1]))
    return numbers


def get_number(data, numbers_positions):
    numbers = []
    found = set()
    for positions in numbers_positions:
        for position in positions:
            number = []
            pos_col = position[1]
            pos_row = position[0]
            while data[pos_row][pos_col].isdigit() and 0 <= pos_col < len(data[0]):
                pos_col -= 1
            pos_col += 1
            while 0 <= pos_col < len(data[0]) and data[pos_row][pos_col].isdigit() and (pos_row, pos_col) not in found:
                found.add((pos_row, pos_col))
                number.append(data[pos_row][pos_col])
                pos_col += 1
            if number:
                numbers.append(int(''.join(number)))
    return tuple(numbers)


def first():
    data = get_data()
    numbers_positions = []
    for idx1, line in enumerate(data):
        for idx2, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue
            else:
                numbers_positions.append(check_nearby_numbers(data, idx1, idx2))

    numbers = get_number(data, numbers_positions)
    return sum(numbers)


def check_numbers(data, row, column):
    numbers = set()
    positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for pos in positions:
        if 0 <= row + pos[0] < len(data) and \
                0 <= column + pos[1] < len(data[0]) and \
                data[row + pos[0]][column + pos[1]].isdigit():
            numbers.add(get_number(data, [[(row + pos[0], column + pos[1])]]))
    if len(numbers) != 2:
        return 0
    res = 1
    for arr in numbers:
        for num in arr:
            res *= num
    return res


def second():
    data = get_data()
    numbers = []
    for idx1, line in enumerate(data):
        for idx2, char in enumerate(line):
            if char.isdigit() or char != '*':
                continue
            else:
                numbers.append(check_numbers(data, idx1, idx2))

    return sum(numbers)


if __name__ == '__main__':
    print(first())
    print(second())