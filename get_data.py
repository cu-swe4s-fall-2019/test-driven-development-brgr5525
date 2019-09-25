import sys


def read_stdin_col(col_num):
    file_name = sys.stdin

    try:
        f = open(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')
    num = 0
    L = []

    for l in f:
        A = l.rstrip().split(',')
        try:
            L.append(int(A[col_num]))
        except IndexError:
            f.close()
            return None
        except ValueError:
            f.close()
            return None
        num += 1

    f.close()

    if num == 0:
        return None

    return L
