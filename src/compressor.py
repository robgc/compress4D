max_pair = 0
max_odd = 0
d3_cells = list()
d2_cells = list()
d1_cells = list()


def is_max(n):
    return n == max_pair or n == max_odd


def generate_4d_indices(size):
    global max_pair
    max_pair = size * 2
    res = [2] * 4
    l_max = [max_pair] * 4
    while res != l_max:
        yield tuple(res)
        if not is_max(res[3]):
            res[3] += 2
        elif not is_max(res[2]) and is_max(res[3]):
            res[2] += 2
            res[3] = 2
        elif not is_max(res[1]) and (is_max(res[2]) and is_max(res[3])):
            res[1] += 2
            res[2] = 2
            res[3] = 2
        elif is_max(res[1]) and is_max(res[2]) and is_max(res[3]):
            res[0] += 2
            res[1] = 2
            res[2] = 2
            res[3] = 2
    yield tuple(res)
    return


def generate_3d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 3 + [1]
    l_max = [max_odd] + [max_pair] * 3
    while res != l_max:
        yield tuple(res)
        if not is_max(res[3]):
            res[3] += 2
        elif not is_max(res[2]) and is_max(res[3]):
            res[2] += 2
            res[3] = 1 if res[3] % 2 else 2
        elif not is_max(res[1]) and (is_max(res[2]) and is_max(res[3])):
            res[1] += 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (not is_max(res[0]) and
              is_max(res[1])and is_max(res[2]) and is_max(res[3])):
            res[0] += 2
            res[1] = 1 if res[1] % 2 else 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (is_max(res[0]) and
              is_max(res[1]) and is_max(res[2]) and is_max(res[3])):
            if res[3] % 2:
                res = [2, 2, 1, 2]
            elif res[2] % 2:
                res = [2, 1, 2, 2]
            elif res[1] % 2:
                res = [1, 2, 2, 2]
    yield tuple(res)
    return


def generate_2d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 2 + [1] * 2
    l_max = [max_odd] * 2 + [max_pair] * 2
    while res != l_max:
        yield tuple(res)
        if not is_max(res[3]):
            res[3] += 2
        elif not is_max(res[2]) and is_max(res[3]):
            res[2] += 2
            res[3] = 1 if res[3] % 2 else 2
        elif not is_max(res[1]) and (is_max(res[2]) and is_max(res[3])):
            res[1] += 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (not is_max(res[0]) and
              is_max(res[1])and is_max(res[2]) and is_max(res[3])):
            res[0] += 2
            res[1] = 1 if res[1] % 2 else 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (is_max(res[0]) and
              is_max(res[1]) and is_max(res[2]) and is_max(res[3])):
            if res[3] % 2:
                if res[2] % 2:
                    res = [2, 1, 2, 1]
                elif res[1] % 2:
                    res = [1, 2, 2, 1]
                elif res[0] % 2:
                    res = [2, 1, 1, 2]
            elif res[2] % 2:
                if res[1] % 2:
                    res = [1, 2, 1, 2]
                else:
                    res = [1, 1, 2, 2]
    yield tuple(res)
    return


def generate_1d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 1 + [1] * 3
    l_max = [max_odd] * 3 + [max_pair] * 1
    while res != l_max:
        yield tuple(res)
        if not is_max(res[3]):
            res[3] += 2
        elif not is_max(res[2]) and is_max(res[3]):
            res[2] += 2
            res[3] = 1 if res[3] % 2 else 2
        elif not is_max(res[1]) and (is_max(res[2]) and is_max(res[3])):
            res[1] += 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (not is_max(res[0]) and
              is_max(res[1])and is_max(res[2]) and is_max(res[3])):
            res[0] += 2
            res[1] = 1 if res[1] % 2 else 2
            res[2] = 1 if res[2] % 2 else 2
            res[3] = 1 if res[3] % 2 else 2
        elif (is_max(res[0]) and
              is_max(res[1]) and is_max(res[2]) and is_max(res[3])):
            if not res[0] % 2:
                res = [1, 2, 1, 1]
            elif not res[1] % 2:
                res = [1, 1, 2, 1]
            elif not res[2] % 2:
                res = [1, 1, 1, 2]
    yield tuple(res)
    return


def generate_0d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [1] * 4
    l_max = [max_odd] * 4
    while res != l_max:
        yield tuple(res)
        if not is_max(res[3]):
            res[3] += 2
        elif not is_max(res[2]) and is_max(res[3]):
            res[2] += 2
            res[3] = 1
        elif not is_max(res[1]) and (is_max(res[2]) and is_max(res[3])):
            res[1] += 2
            res[2] = 1
            res[3] = 1
        elif is_max(res[1]) and is_max(res[2]) and is_max(res[3]):
            res[0] += 2
            res[1] = 1
            res[2] = 1
            res[3] = 1
    yield tuple(res)
    return


def is_adyacent(tuple1, tuple2):
    res = 0
    for index in range(0, 4):
        res += abs(tuple1[index] - tuple2[index])
    return res == 1


def get_from_matrix(tuple, matrix):
    i, j, k, l = (int((tuple[0] / 2) - 1), int((tuple[1] / 2) - 1),
                  int((tuple[2] / 2) - 1), int((tuple[3] / 2) - 1))
    return matrix[i][j][k][l] == 1


def get_m43(size, matrix):
    global d3_cells
    i, j = 0, 0
    res = list()

    tuple_4d = generate_4d_indices(size)
    tuple_3d = generate_3d_indices(size)

    for x in tuple_4d:
        if get_from_matrix(x, matrix):
            j = 0
            for y in tuple_3d:
                if is_adyacent(x, y):
                    d3_cells.append(y)
                    res.append((i, j))
                j += 1
        i += 1
        tuple_3d = generate_3d_indices(size)

    return res
