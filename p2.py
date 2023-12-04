def get_data(name):
    with open(name) as f:
        for line in f.readlines():
            yield line.strip()


def parse_line():
    for line in get_data('p2_data.txt'):
        game, cubes = line.split(':')
        game_id = game.split(' ')[1]
        arr = []
        for num_of_cubes in cubes.strip().split(';'):
            d = {}
            for color in num_of_cubes.strip().split(','):
                cube = color.strip().split()
                d[cube[1]] = int(cube[0])
            arr.append(d)
        yield [arr, int(game_id)]


def is_not_valid_amount(cubes, color):
    threshold = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    return color in cubes and cubes[color] > threshold[color]


def is_valid_game(game):
    for cubes in game:
        if is_not_valid_amount(cubes, 'red') or is_not_valid_amount(cubes, 'green') or \
                is_not_valid_amount(cubes, 'blue'):
            return False
    return True


def first():
    res = 0
    for line in parse_line():
        game_id = line.pop()
        for game in line:
            if is_valid_game(game):
                res += game_id
    print(res)


def second():
    res = 0
    for line in parse_line():
        line.pop()
        red = []
        blue = []
        green = []
        for game in line:
            for cubes in game:
                if 'red' in cubes:
                    red.append(cubes['red'])
                if 'blue' in cubes:
                    blue.append(cubes['blue'])
                if 'green' in cubes:
                    green.append(cubes['green'])
        res += (max(red) * max(green) * max(blue))
    print(res)


if __name__ == '__main__':
    print(first())
    print(second())