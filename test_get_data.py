import unittest
import get_data
import sys


class TestGetData(unittest.TestCase):

    def test_read_stdin_col_no_file(self):
        sys.stdin = 'no_file.csv'

        with self.assertRaises(FileNotFoundError) as ex:
            get_data.read_stdin_col(0)

        self.assertEqual(str(ex.exception), sys.stdin + ' not found.')

    def test_read_stdin_col_empty_file(self):
        sys.stdin = 'empty_file.csv'
        f = open(sys.stdin, 'w')
        f.close()

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, None)

    def test_read_stdin_col_1st_col_constant(self):
        sys.stdin = 'test.csv'
        f = open(sys.stdin, 'w')
        f.write('1\n1\n1\n1\n1')
        f.close()

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, [1, 1, 1, 1, 1])

    def test_read_stdin_col_2nd_col_constant(self):
        sys.stdin = 'test.csv'
        f = open(sys.stdin, 'w')
        f.write('1,2\n1,2\n1,2\n1,2\n1,2')
        f.close()

        L = get_data.read_stdin_col(1)
        self.assertEqual(L, [2, 2, 2, 2, 2])

    def test_read_stdin_col_index_out_of_range(self):
        sys.stdin = 'test.csv'
        f = open(sys.stdin, 'w')
        f.write('1,2\n1,2\n1,2\n1,2\n1,2')
        f.close()

        L = get_data.read_stdin_col(4)
        self.assertEqual(L, None)

    def test_read_stdin_col_non_num_chars(self):
        sys.stdin = 'test.csv'
        f = open(sys.stdin, 'w')
        f.write('1,2\n1,2\n1,2\n1,2\nx,2')
        f.close()

        L = get_data.read_stdin_col(0)
        self.assertEqual(L, None)


if __name__ == '__main__':
    unittest.main()
