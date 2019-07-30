#!/usr/bin/env python3

"""
Email parsing!
"""

import sys

def extract_hostname(line):
    index = line.find('@')
    if index == -1:
        return ''
    else:
        i = index + 1
        while i < len(line) and line[i] != ' ':
            if line[i].isalpha or line[i] == '.':
                i += 1
            else:
                break
        hostname = line[index + 1:i]
    if len(hostname) <= 4 or not '.' in hostname:
        return ''
    return hostname

def extract_all_hostnames(filename):
    """
    Given a file, parse through all lines in the file and extract all hostnames
    from valid email addresses.
    Then, print sorted the list of all unique hostnames found in the file.
    SOLUTION to emails.txt input:
    ['d.tv', 'gmail.com', 'spam.com', 'stanford.edu', 'yahoo.com']
    """
    hostnames = []
    with open(filename, 'r') as f:
        for line in f:
            hostname = extract_hostname(line)
            if hostname != '' and not hostname in hostnames:
                hostnames.append(hostname)
    return sorted(hostnames)


def main():
    """
    # Calls to extract_all_hostnames()
    # with command line arg.
    args = sys.argv[1:]
    # args[0] is filename
    if len(args) == 1:
        extract_all_hostnames(args[0])
    else:
        print('usage: python3 email_parser.py filename-to-read')
    """
    print(extract_all_hostnames('emails.txt'))

# Python boilerplate
if __name__ == "__main__":
    main()
