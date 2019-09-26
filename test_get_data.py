import unittest
import get_data
import sys
from io import StringIO


class TestGetData(unittest.TestCase):

    def test_read_stdin_col_stdin_is_None(self):
        sys.stdin = None

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, None)

    def test_read_stdin_col_1st_col_constant(self):
        sys.stdin = StringIO('1\n1\n1\n1\n1')

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, [1, 1, 1, 1, 1])

    def test_read_stdin_col_2nd_col_constant(self):
        sys.stdin = StringIO('1 2\n1 2\n1 2\n1 2\n1 2')

        L = get_data.read_stdin_col(1)
        self.assertEqual(L, [2, 2, 2, 2, 2])

    def test_read_stdin_col_index_out_of_range(self):
        sys.stdin = StringIO('1 2\n1 2\n1 2\n1 2\n1 2')

        L = get_data.read_stdin_col(4)
        self.assertEqual(L, None)

    def test_read_stdin_col_non_num_chars(self):
        sys.stdin = StringIO('1 2\n1 2\n1 2\n1 2\nx 2')

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, None)


if __name__ == '__main__':
    unittest.main()
