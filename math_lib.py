"""Different math and analysis functions

    * list_mean - returns the arithmetic mean of an array
    * list_stdev - returns the arithmetic standard deviation of an array
"""
import math


def list_mean(L):
    """Compute the arithmetic mean of an array. Expects a non-empty array.

    Parameters
    __________
    L : list of int and float
        Non-empty list containing numbers whose mean is desired.

    Returns
    _______
    float
        Mean of the values in L.
    None
        Returns 'None' if L is null or empty.

    Raises
    ______
    ValueError
        Occurs when there is a non -int or -float value in L.
    """
    if L is None:
        return None

    if len(L) == 0:
        return None

    sum = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Mean undefined. Unsupported value in L.')
        sum += l

    return sum/len(L)


def list_stdev(L):
    """Compute the standard deviation of an array. Expects a non-empty array.

    Parameters
    __________
    L : list of int and float
        Non-empty list containing numbers whose stdev is desired.

    Returns
    _______
    float
        Standard deviation of the values in L based on mean.
    None
        Returns 'None' if L contains a single element or list_mean(L) is None.

    Raises
    ______
    ValueError
        Occurs when there is a non -int or -float value in L.
    """
    try:
        m = list_mean(L)
    except ValueError:
        raise ValueError('Mean and Stdev undefined. Unsupported value in L.')

    if m is None:
        return None

    if len(L) == 1:
        return None

    sum = 0
    for l in L:
        sum += (m - l) ** 2

    return math.sqrt(sum/(len(L)-1))
