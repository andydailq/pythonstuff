"""
File: similarity.py
------------------------
This file should implement a console program that prompts users
for a DNA strand that they want to search through and a DNA target strand
that they want to search for. The program then outputs the closest match
to the target strand, as defined by the similarity metric.
"""

def search_sequence(dna_to_match, subsequence):
    """
    This function takes in two DNA sequences, and calculates
    the number of spots at which the two sequences have the same
    base pairs.
    >>> search_sequence("GATC", "AATC")
    3
    >>> search_sequence("AGC", "TAG")
    0
    >>> search_sequence("ac","AC")
    2
    >>> search_sequence("TcGaC","GGaCT")
    0
    >>> search_sequence("tcAAtgGcC", "TGaATGatc")
    6
    """
    count = 0
    for i in range(len(dna_to_match)):
        if dna_to_match[i].upper() == subsequence[i].upper():
            count += 1
    return count

def find_best_substrand(dna_to_match, dna_to_search):
    """
    This function takes in two DNA strands, one to search through and one
    for which you are trying to find a match. The function returns the closest
    match to the target sequence in the search sequence based on the counter
    value, the higher the value, the closer the match is.
    >>> find_best_substrand("TCATA","ATGCCTGATA")
    'TGATA'
    >>> find_best_substrand("", "ATGCCTGATA")
    ''
    >>> find_best_substrand("tca","TCg")
    'TCG'
    >>> find_best_substrand("ACT","AGTCCGT")
    'AGT'
    >>> find_best_substrand("t","AGCCG")
    ''
    """
    matchlength = len(dna_to_match)
    if matchlength == 0:
        return ''
    max = 0
    closest_match = ''
    for i in range(len(dna_to_search) - matchlength + 1):
        current_substring = dna_to_search[i:i + matchlength].upper()
        counter = search_sequence(dna_to_match, current_substring)
        if counter > max:
            closest_match = current_substring
            max = counter
    return closest_match

def main():
    """
    Establish user interface to input DNA sequence to search from
    and input the matching DNA the user wants. The output is given
    via the 2 functions previously defined and returns the closest
    match to the console.
    """
    seq_to_search = input("Please give me a DNA sequence to search: ")
    seq_for_matching = input("What DNA sequence would you like me to match? ")
    best_match = find_best_substrand(seq_for_matching, seq_to_search)

    print("The best match is " + best_match)

if __name__ == "__main__":
    main()
