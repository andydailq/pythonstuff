"""
For this problem, we'll say that the text of an int "number"
can optionally contain commas, like '1,200' or '2,,,3,4' or '42'.
The rightmost char of the number will always be a digit,
but everywhere else there can be commas mixed in.

Given a string s, find the last number-with-commas in s, 
and return it as a string. If there is no such number in s,
return the empty string.

So for example ...

'xx 11 22 1,200 xx' -> '1,200'
'xx 11 22 yyy' -> '22'
'xx 1,2 x ,99,,2,3 z' -> ',99,,2,3'
'abcxyz' -> ''
"""
def parse1(s):
    right = s.len() - 1
    while right >=0 and not s[right].isdigit():
        right -= 1

    if right == -1:
        return ''

    left = right - 1
    while left >= 0 and (s[left].isdigit() or s[left]==','):
        left -= 1

    return s[left+1:right+1]