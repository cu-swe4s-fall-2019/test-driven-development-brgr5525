import math

def list_mean(L):
    if L is None:
        return None

    if len(L) == 0:
        return None

    sum = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Mean undefined. Unsupported value in list.')
        sum += l

    return sum/len(L)


def list_stdev(L):
    #math.sqrt(sum([(m-x)**2 for x in L]) / len(L))
    try:
        m = list_mean(L)
    except ValueError:
        raise ValueError('Stdev undefined. Unsupported value in list.')

    if m is None:
        return None

    if len(L) == 1:
        return None

    sum = 0
    for l in L:
        sum += (m - l) ** 2

    return math.sqrt(sum/(len(L)-1))
