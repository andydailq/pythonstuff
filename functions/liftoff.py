"""
File: liftoff.py
--------------------
This file should define a simple program that displays
a rocket launch countdown.
"""

def main():
    """
    The program runs a countdown time from 10 down to 1 and prints Takeoff.
    Pre-cond.: Output is nothing
    Post-cond.: Outputs a list of numbers descending from 10 to 1 and ends the list with the string 'Takeoff'
    """
    count = 9
    for i in range(1,11):
        value = i + count
        print(value)
        count = count - 2
    print("Liftoff")

if __name__ == "__main__":
    main()
