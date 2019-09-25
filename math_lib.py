
def list_mean(L):
    if L is None:
        return None

    if len(L) == 0:
        return None

    sum = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Mean undefined. Unsuported value in list.')
        sum += l

    return sum/len(L)


def list_stdev(L):
    return None
