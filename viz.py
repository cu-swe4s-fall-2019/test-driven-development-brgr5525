"""Script to run various methods for data visualization
"""
import argparse
import sys
import get_data
import data_viz


def main():
    parser = argparse.ArgumentParser(
                description='Input output file name and desired visualization',
                prog='viz.py')
    parser.add_argument('--out_file',
                        type=str,
                        help='Name of output file',
                        required=True)
    parser.add_argument('--plot_type',
                        type=str,
                        help='Type of visualization',
                        required=True)
    args = parser.parse_args()

    L = get_data.read_stdin_col(0)

    if L is None:
        print('Data could not be extracted properly. Check input data type.')
        sys.exit(1)

    viz = args.plot_type
    out = args.out_file

    try:
        if viz == 'Boxplot':
            data_viz.boxplot([], out)
        elif viz == 'Histogram':
            data_viz.histogram(L, out)
        elif viz == 'Combo':
            data_viz.combo(L, out)
        else:
            print("When calling viz.py --plot_type must be" +
                  " 'Boxplot', 'Histogram', or 'Combo'")
            sys.exit(1)
    except ValueError as ex:
        print('--out_file_name does not have proper file extension')
        sys.exit(1)
    except SystemExit:
        print(str(out) + ' already exists.')
        sys.exit(1)
    except TypeError as ex:
        print('No output file name was given.')
        sys.exit(1)


if __name__ == '__main__':
    main()
