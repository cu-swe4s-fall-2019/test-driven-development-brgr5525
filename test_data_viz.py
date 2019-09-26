import unittest
import data_viz
import sys


class TestDataViz(unittest.TestCase):

    def test_data_viz_no_out_file_name(self):
        L = []

        with self.assertRaises(TypeError) as ex:
            data_viz.boxplot(L, None)

        self.assertEqual(str(ex.exception), 'No file name given.')

    def test_data_viz_file_already_exits(self):
        L = []
        file_name = 'test.png'
        f = open(file_name, 'w')
        f.close()

        with self.assertRaises(SystemExit) as ex:
            data_viz.boxplot(L, file_name)

        self.assertEqual(str(ex.exception), 'File already exists.')


if __name__ == '__main__':
    unittest.main()
