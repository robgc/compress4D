

max_pair = 0
max_odd = 0


def is_max(n):
    return n == max_pair or n == max_odd


def generate_4d_indices(size):
    global max_pair
    max_pair = size * 2
    res = [2] * 4
    l_max = [max_pair] * 4
    while res != l_max:
        yield res
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
    yield res
    return


def generate_3d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 3 + [1]
    l_max = [max_odd] + [max_pair] * 3
    while res != l_max:
        yield res
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
    yield res
    return


def generate_2d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 2 + [1] * 2
    l_max = [max_odd] * 2 + [max_pair] * 2
    while res != l_max:
        yield res
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
    yield res
    return


def generate_1d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [2] * 1 + [1] * 3
    l_max = [max_odd] * 3 + [max_pair] * 1
    while res != l_max:
        yield res
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
    yield res
    return


def generate_0d_indices(size):
    global max_pair, max_odd
    max_pair = size * 2
    max_odd = max_pair + 1
    res = [1] * 4
    l_max = [max_odd] * 4
    while res != l_max:
        yield res
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
    yield res
    return
