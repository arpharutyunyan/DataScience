import sys
import csv
import random
import numpy as np

"""
Commands are: 'open' for creating file
              'read' for reading and printing the result
"""


def main():
    # check if there is command
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit('Usage: You should choose one command from [open, read]')
    command = sys.argv[1]
    if command == 'open':
        open_file()
    elif command == 'read':
        read_file(file='csv_file.csv')
    else:
        sys.exit(f'Usage: Command {command} not found')


def open_file():
    """
    The function should create a csv file, write rows and columns as an array with 200 elements
    """
    # open file or create, if there is no a file with that name
    with open('csv_file.csv', 'w') as f:
        # write tab between elements in row
        csv_writer = csv.writer(f, delimiter='\t')
        # to go over the rows with loop and write randomly chosen element in columns
        for row in range(50):
            csv_writer.writerow([random.randrange(0, 200) for col in range(4)])
    print('The file is ready for reading.')


def read_file(file):
    """
    The function should read the given file as an array and return the odd numbers
    """
    try:
        # if file is already exist
        with open(file, 'r') as f:
            # read file as a list
            csv_reader = list(csv.reader(f, delimiter='\t'))
    except:
        # if the file is not creating
        with open(file, 'a+') as f:
            # read file as a list
            csv_reader = list(csv.reader(f, delimiter='\t'))

    if len(csv_reader) == 0:
        raise Exception("First use command 'open'")
    # convert list into array
    csv_reader = np.array(csv_reader, dtype=int)
    # to get each element
    print('The odd numbers are: ')
    for elem in csv_reader.flat:
        # check if element is odd
        if elem % 2 != 0:
            print(elem, '\t', end=' ')


if __name__ == '__main__':
    main()
