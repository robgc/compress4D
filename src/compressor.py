max_pair = 0
max_odd = 0
d3_cells = list()
d2_cells = list()
d1_cells = list()
d0_cells = list()


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


def get_m32(size, matrix):
    global d3_cells, d2_cells
    i, j = 0, 0
    res = list()

    tuple_3d = d3_cells
    tuple_2d = generate_2d_indices(size)

    for x in tuple_3d:
        j = 0
        for y in tuple_2d:
            if is_adyacent(x, y):
                d2_cells.append(y)
                res.append((i, j))
            j += 1
        i += 1
        tuple_2d = generate_2d_indices(size)

    return res


def get_m21(size, matrix):
    global d2_cells, d1_cells
    i, j = 0, 0
    res = list()

    tuple_2d = d2_cells
    tuple_1d = generate_1d_indices(size)

    for x in tuple_2d:
        j = 0
        for y in tuple_1d:
            if is_adyacent(x, y):
                d1_cells.append(y)
                res.append((i, j))
            j += 1
        i += 1
        tuple_1d = generate_1d_indices(size)

    return res


def get_m10(size, matrix):
    global d1_cells, d0_cells
    i, j = 0, 0
    res = list()

    tuple_1d = d1_cells
    tuple_0d = generate_0d_indices(size)

    for x in tuple_1d:
        j = 0
        for y in tuple_0d:
            if is_adyacent(x, y):
                d0_cells.append(y)
                res.append((i, j))
            j += 1
        i += 1
    tuple_0d = generate_0d_indices(size)

    return res


def test_list(tuple1, tuple2):
    a1, a2, b1, b2 = 0,0,0,0
    count1, count2 = 0,0
    test = False;
    for x in tuple1:
        a1, b1 = x[0], x[1]
        count1, count2 = 0,0
        for y in tuple2:
            a2, b2 = y[0], y[1]
            if(a1 == b2):
                count1 += 1
            if(a2 == b1):
                count2 += 1
        if ( count1 > 1 or count2 >1):
            test = True
            break
    return test


def csr(size, matrix):
    m43 = get_m43(size, matrix)
    m32 = get_m32(size, matrix)
    m21 = get_m21(size, matrix)
    m10 = get_m10(size, matrix)

    return m43, m32, m21, m10
