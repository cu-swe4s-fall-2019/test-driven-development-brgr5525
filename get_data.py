"""Function to get get_data

    * read_stdin_col - reads data from STDIN and returns an array of numbers

"""
import sys


def read_stdin_col(col_num):
    """Read STDIN and extracts data from specified column to return

    Parameters
    __________
    col_num : int
        Number of column containing desired data.

    Returns
    _______
    L : array of numbers
        Array containing numbers from specified column of standard in.
    None
        Returns 'None' in the case that numerical data cannot be extracted.
    """
    if sys.stdin is None:
        return None
    num = 0
    L = []
    for l in sys.stdin:
        try:
            A = [int(x) for x in l.split()]
            L.append(int(A[col_num]))
        except IndexError:
            return None
        except ValueError:
            return None

    return L
