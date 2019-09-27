# test-driven-dev
Test Driven Development

## Created Modules
1. list_mean(L)
2. list_stdev(L)
3. read_stdin_col(col_num)
4. boxplot(L, out_file_name)
5. histogram(L, out_file_name)
6. combo(L, out_file_name)

## Testing
- Added unit testing for each module listed above
- All modules were designed using unit testing and TDD

## viz.py
- Created script that utilized each module to produce desired visualization of dat
- Takes data from STDIN
- Takes in-line commands from user to specify visualization type and name of the file that is being created
- example function call:
    python viz.py --out_file 'FileName.png' --plot_type 'Histogram'
- plot_type takes one of three options: 'Histogram', 'Boxplot', 'Combo'
- out_file takes files with extensions like .png, .pdf, .txt
    - if no extension is specified the default is .png
