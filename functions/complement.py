"""
File: complement.py
-----------------------
This file should define a console program that prompts a user for
a strand of DNA and displays the complement of that strand of DNA.
"""


def build_complement(strand):
    """
    This function takes in a DNA strand and returns the
    complementary DNA strand, as defined by the base pair
    matchings outlined in the Assignment 2 handout.
    Input: The letters AGCT and agct are inputted
    in any order and of any length.
    Output: The complement of that base following the A:T
    and C:G pairing system is outputted and added to the string
    complement. The approached use are a variety of if-elif statements.
    >>> build_complement("ATGCAAG")
    'TACGTTC'
    >>> build_complement("AAAA")
    'TTTT'
    >>> build_complement("TTTT")
    'AAAA'
    >>> build_complement("GC")
    'CG'
    >>> build_complement("GgTTaCTG")
    'CCAATGAC'
    """
    complement = ''
    for i in range(len(strand)):
        letter = strand[i].upper()
        if letter == 'A':
            complement += 'T'
        elif letter == 'T':
            complement += 'A'
        elif letter == 'G':
            complement += 'C'
        elif letter == 'C':
            complement += 'G'
    return complement

def main():
    """
    The input asks for a DNA strand assuming all
    of the base pairs of the input string are valid
    DNA base pairs. The complement base-pair string
    are then printed using concatenation of strings.
    """
    get_string = input("Please give me a DNA strand and I'll find the complement: ")
    processedstr = build_complement(get_string)
    print("The complement of " + get_string + " is " + processedstr)

if __name__ == "__main__":
    main()