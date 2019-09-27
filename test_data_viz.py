import unittest
import data_viz
import sys
import os


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
