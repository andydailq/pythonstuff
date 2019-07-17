"""
File: hailstone.py
-----------------------
This function should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter.
"""

def main():
    """
    Using the hailstone process:
    take any integer and multiply
    by 3 and add 1 if its odd and
    divide by 2 if it's even to
    reduce that said integer down to 1
    Inputs: any positive integer
    Output: the integer 1
    The function round() was never taught
    but I have learned Python before
    and have used it to get rid of the
    decimal 0 outputs when dividing or multiplying.
    """
    num_to_start = int(input("Enter a number: "))
    count = 0
    while num_to_start != 1:
        if num_to_start % 2 == 0:
            originalnum = round(num_to_start)
            num_to_start = round(num_to_start / 2)
            print(str(originalnum) + " is even, so I take half: " + str(num_to_start))
            count += 1
        else:
            originalnum = round(num_to_start)
            num_to_start = round((3 * (num_to_start)) + 1)
            print(str(originalnum) + " is odd, so I make 3n + 1: " + str(num_to_start))
            count += 1
    print("The process took " + str(count) + " step(s) to reach 1.")

if __name__ == "__main__":
    main()
