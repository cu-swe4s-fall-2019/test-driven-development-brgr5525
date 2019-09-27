import unittest
import get_data
import math_lib
import random as rd
import statistics as stats
import math as m
import data_viz
import os
import viz
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


class TestMathLib(unittest.TestCase):

    # UNIT TESTS FOR list_mean
    def test_list_mean_no_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_empty_list(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)

    def test_list_mean_const(self):
        r = math_lib.list_mean([1, 1, 1])
        self.assertEqual(r, 1)

    def test_list_mean_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.randint(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.uniform(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertTrue(m.isclose(r, e))

    def test_list_mean_non_int_in_list(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
        L.append('X')

        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)

        self.assertEqual(str(ex.exception), 'Mean undefined.' +
                                            ' Unsupported value in L.')

    def test_list_mean_zero(self):
        r = math_lib.list_mean([0])
        self.assertEqual(r, 0)

    def test_list_mean_rand_ints_and_floats(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
            L.append(rd.uniform(0, 100))

        r = math_lib.list_mean(L)
        e = stats.mean(L)
        self.assertTrue(m.isclose(r, e))

    def test_list_mean_many_rand_ints_and_floats(self):
        for i in range(1000):
            L = []

            for j in range(10):
                L.append(rd.randint(0, 100))
                L.append(rd.uniform(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertTrue(m.isclose(r, e))

    # UNIT TESTS FOR list_stdev
    def test_list_stdev_no_list(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)

    def test_list_stdev_empty_list(self):
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)

    def test_list_stdev_const(self):
        r = math_lib.list_stdev([1, 1, 1, 1])
        self.assertEqual(r, 0)

    def test_list_stdev_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.randint(0, 100))

            r = math_lib.list_stdev(L)
            e = stats.stdev(L)
            self.assertTrue(m.isclose(r, e))

    def test_list_stdev_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.uniform(0, 100))

            r = math_lib.list_stdev(L)
            e = stats.stdev(L)
            self.assertTrue(m.isclose(r, e))

    def test_list_stdev_non_int_in_list(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
        L.append('X')

        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev(L)

        self.assertEqual(str(ex.exception), 'Mean and Stdev undefined.' +
                                            ' Unsupported value in L.')

    def test_list_stdev_single_element_list(self):
        r = math_lib.list_stdev([1])
        self.assertEqual(r, None)

    def test_list_stdev_rand_ints_and_floats(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
            L.append(rd.uniform(0, 100))

        r = math_lib.list_stdev(L)
        e = stats.stdev(L)
        self.assertTrue(m.isclose(r, e))

    def test_list_stdev_many_rand_ints_and_floats(self):
        for i in range(1000):
            L = []

            for j in range(10):
                L.append(rd.randint(0, 100))
                L.append(rd.uniform(0, 100))

            r = math_lib.list_stdev(L)
            e = stats.stdev(L)
            self.assertTrue(m.isclose(r, e))


class TestDataViz(unittest.TestCase):

    def test_boxplot_no_out_file_name(self):
        L = []

        with self.assertRaises(TypeError) as ex:
            data_viz.boxplot(L, None)

        self.assertEqual(str(ex.exception), 'No file name given.')

    def test_boxplot_file_already_exits(self):
        L = []
        file_name = 'test.png'
        f = open(file_name, 'w')
        f.close()

        with self.assertRaises(SystemExit) as ex:
            data_viz.boxplot(L, file_name)

        self.assertEqual(str(ex.exception), 'File already exists.')

    def test_boxplot_file_type_unsupported(self):
        L = [1, 1, 1]

        with self.assertRaises(ValueError) as ex:
            data_viz.boxplot(L, 'test.py')

        self.assertEqual(str(ex.exception), 'Out file type unsupported.')

    def test_boxplot_creates_file(self):
        file_name = 'create.png'
        if os.path.exists(file_name):
            os.remove(file_name)

        self.assertTrue(data_viz.boxplot([1, 1, 1], file_name))

    def test_histogram_no_out_file_name(self):
        L = []

        with self.assertRaises(TypeError) as ex:
            data_viz.histogram(L, None)

        self.assertEqual(str(ex.exception), 'No file name given.')

    def test_histogram_file_already_exits(self):
        L = []
        file_name = 'test.png'
        f = open(file_name, 'w')
        f.close()

        with self.assertRaises(SystemExit) as ex:
            data_viz.histogram(L, file_name)

        self.assertEqual(str(ex.exception), 'File already exists.')

    def test_histogram_file_type_unsupported(self):
        L = [1, 1, 1]

        with self.assertRaises(ValueError) as ex:
            data_viz.boxplot(L, 'test.py')

        self.assertEqual(str(ex.exception), 'Out file type unsupported.')

    def test_histogram_creates_file(self):
        file_name = 'create.png'
        if os.path.exists(file_name):
            os.remove(file_name)

        self.assertTrue(data_viz.histogram([1, 1, 1], file_name))

    def test_combo_no_out_file_name(self):
        L = []

        with self.assertRaises(TypeError) as ex:
            data_viz.combo(L, None)

        self.assertEqual(str(ex.exception), 'No file name given.')

    def test_combo_file_already_exits(self):
        L = []
        file_name = 'test.png'
        f = open(file_name, 'w')
        f.close()

        with self.assertRaises(SystemExit) as ex:
            data_viz.combo(L, file_name)

        self.assertEqual(str(ex.exception), 'File already exists.')

    def test_combo_file_type_unsupported(self):
        L = [1, 1, 1]

        with self.assertRaises(ValueError) as ex:
            data_viz.combo(L, 'test.py')

        self.assertEqual(str(ex.exception), 'Out file type unsupported.')

    def test_combo_creates_file(self):
        file_name = 'create.png'
        if os.path.exists(file_name):
            os.remove(file_name)

        self.assertTrue(data_viz.combo([1, 1, 1], file_name))


if __name__ == '__main__':
    unittest.main()
