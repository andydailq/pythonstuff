"""
Names Search
Program is run from cmd line, check main() for info

"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    """

    if name not in name_data:
        name_data[name] = {year: rank}
    else:
        if year in name_data[name]:
            if name_data[name][year] > rank:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    """
    year = 0
    with open(filename, 'r') as f:
        for line in f:
            split_lst = line.split(',')
            cleaned_lst = []
            for item in split_lst:
                cleaned_lst.append(item.strip())
            if len(cleaned_lst) == 1:
                year = int(cleaned_lst[0])
            else:
                rank = int(cleaned_lst[0])
                add_data_for_name(name_data, year, rank, cleaned_lst[1])
                add_data_for_name(name_data, year, rank, cleaned_lst[2])


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    """
    names_list = []
    for name in name_data:
       if target.lower() in name.lower():
           names_list.append(name)
    return names_list

def print_names(name_data):
    """

    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
