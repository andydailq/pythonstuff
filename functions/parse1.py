"""
Given a string s. For each '@' in s, parse out the substring
of zero or more alphabetic chars which immediately follow the '@',
which we will call a "word". Return a list of all the word substrings
in the order they appear in s, like these examples:

'x @abc @xyz x' -> ['abc', 'xyz']
'xx@xx$$' -> ['xx']
'@a @ @c' -> ['a', '', 'c']
"""

def parse1(s):
    lst = []
    findindex = 0
    while True:
        index = s.find('@', findindex)
        if index == -1:
            break
        end = index + 1
        while end < len(s) and s[end].isalpha():
            end += 1
        lst.append(s[index + 1:end])
        findindex = end
    return lst
