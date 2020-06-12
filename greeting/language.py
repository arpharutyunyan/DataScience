import os
import sys

# get computer name
name = os.uname()[1]


def main():
    # open at least one file
    if len(sys.argv) != 2:
        sys.exit('Choose one text file')
    language = request()
    data = read_file(sys.argv[1])
    # if there isn't key with that language code
    if language not in data:
        raise Exception('Enter correct code.')
    res = data[language]
    print(res)


def read_file(filename):
    """
    Get file.
    Return a dictionary there keys are language codes from given list and
    values are greeting words from txt file.
    """
    data = {}
    languages = ['AM', 'RU', 'EN']
    with open(filename) as f:
        reader = f.readlines()
        for i in range(len(languages)):
            # values should be row in txt file expect the last element (\n)
            # and plus empty string between greeting phrase and computer name
            data[languages[i]] = reader[i][:-1] + ' ' + name
    return data


def request():
    """
    Do request about language codes and return the result.
    """
    language_request = input('{0} what language do you prefer? \n'
                             'Please enter language code (i.e. AM, RU or EN) '.format(name))
    return language_request


if __name__ == '__main__':
    main()
