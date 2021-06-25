import os
import sys
import csv
import argparse

def get_arguments():
    """Grab user supplied arguments using the argparse library."""

    parser = argparse.ArgumentParser()

    parser.add_argument('-i' , '--input_file' , required=True ,
                        help='Csv input file path (With extension)' , type=str)

    parser.add_argument('-o' , '--output_file' , required=True ,
                        help='Csv output file (With extension)' , type=str)

    parser.add_argument('-r' , '--row_limit' , required=True ,
                        help='row limit to split csv at' , type=int)
    parser.add_argument('-d' , '--delimiter' , help='csv delimiter' ,
                        type=str , default=',')
    args = parser.parse_args()

    is_file_exist(parser , args.input_file)

    can_split(parser , args.input_file , args.row_limit)

    return args.input_file, args.output_file, args.row_limit , args.delimiter

def is_file_exist(parser , file_name):
    if not os.path.exists(file_name):
        parser.error(f"The file {file_name} doesn't exist")
        sys.exit(1)
def can_split(parser , input_file , row_limit):
    """
    Ensure that the # of rows in the input_file
    is greater than the row_limit.
    """
    row_count = 0

    for row in csv.reader( open(input_file) ):
        row_count += 1

    if row_limit > row_count:
        parser.error( f"The 'row_count' of '{row_limit}' is > the number of rows in '{input_file}'!")
        sys.exit(1)
def parse_file(args):
    """
    Splits the CSV into multiple files or chunks based on the row_limit.
    Then create new CSV files.
    """
    input_file = args[0]
    output_file = args[1]
    row_limit = args[2]
    delimiter = args[3]
    output_path = '.'  # Current directory

    # Read CSV, split into list of lists
    with open(input_file , mode='r') as csv_file:
        csv_reader = csv.reader( csv_file , delimiter= delimiter)
        rows = []
        for row in csv_reader:
            rows.append(row)
        #extract the header
        header = rows.pop(0)

        # Split list of list into chunks
        current_chunk = 1
        for i in range(0 , len(rows) , row_limit):
            chunk = rows[i: i + row_limit]

            # Create new output file
            current_output = os.path.join(output_path , f'{output_file}{current_chunk}.csv')

            #add the header to each file
            chunk.insert(0, header)

            # Write chunk to output file
            with open(current_output , mode='w') as output_csv:
                writer = csv.writer(output_csv , delimiter=delimiter)

                writer.writerow(chunk)

            # Create new chunk
            current_chunk += 1

def main():
    parse_file(get_arguments())

if __name__ == '__main__':
    main()
