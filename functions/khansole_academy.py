"""
File: khansole_academy.py
---------------------------

"""

import random
import math

TOTAL_PROBLEMS = 5
MIN_THRESHOLD = 0
MAX_THRESHOLD = 30

min_threshold_for_dna = 4
max_threshold_for_dna = 10


def user_prompt():
    """
    This function returns the prompt that the user is presented with to choose
    what kind of problem they want to practice.
    """
    return """
    Enter enter the number of the type of arithmetic problem you want to practice.
    1) Addition
    2) Subtraction
    3) Pythagorean Theorem
    4) DNA Complements
    """


def generate_input():
    """
    This function generates a random number to act as input for an
    arithmetic problem. For more documentation on the Python random module, go
    to this link: https://docs.python.org/3.7/library/random.html
    """
    return random.randint(MIN_THRESHOLD, MAX_THRESHOLD)


def generate_letters():
    """
    This function generates a random sequence of letters to act as input for an
    DNA nucleotide base-pairing problem. The use of join() to create a random letter
    between lengths 4 to 10 was searched up on https://www.pythonprogramming.in/generate-random-string-of-n-characters.html
    >>> generate_letters()
    'ATTC'
    """
    return ''.join(random.choice("ATGC") for i in range(random.randint(min_threshold_for_dna, max_threshold_for_dna)))

def create_arithmetic_problem_prompt(a, b, operator):
    """
    This function takes in two numbers and an operator and returns a string
    that is built from these three pieces of information
    """
    return "What is " + str(a) + " " + operator + " " + str(b) + "?"


def create_pythagorean_problem_prompt(a, b):
    """
    This function takes in two numbers and returns a string
    that is built from these three pieces of information
    >>> create_pythagorean_problem_prompt(3,4)
    'What is 3 squared + 4 squared rounded to the nearest 2 decimal places?'
    """
    return "What is " + str(a) + " squared + " + str(b) + " squared rounded to the nearest 2 decimal places?"


def create_dna_problem_prompt(a):
    """
    This function takes in a DNA sequence and outputs a string.
    >>> create_dna_problem_prompt('ATCC')
    'What is the DNA base-pair complement of ATCC?'
    """
    return "What is the DNA base-pair complement of " + str(a) + "?"


def assess_user_response(user_answer, true_answer):
    """
    This function takes in two answers, one of which is provided by
    the user and one of which is the correct answer. It generates an
    appropriate response depending on whether or not the user answers
    matches the correct answer.
    """
    if user_answer == true_answer:
        print("Correct, great work!")
        return True
    else:
        print("Incorrect. The expected answer was " + str(true_answer))
        return False


def addition(a, b):
    """
    Simple function to encapsulate addition
    """
    return a + b


def subtraction(a, b):
    """
    Simple function to encapsulate subtraction
    """
    return a - b

def pythag(a, b):
    """
    Simple function to encapsulate the use of Pythagorean Theorem
    >>> pythag(3,4)
    5.0
    """
    c = round(math.sqrt(a*a + b*b), 2)
    return c


def build_complement(strand):
    """
    The DNA complement finding function. The expected input of the complement
    DNA base-pair should be inputted in capital.
    >>> build_complement('AGTC')
    'TCAG'
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
    This console program currently implements some of the basic functionality
    of Khansole Academy. It currently supports 4 problem types (addition,
    subtraction, use Pythagorean Theorem to find hypotenuse, and finding DNA complements)
    and keeps track of how many problems the user gets correct.
    """
    num_problems_done = 0
    num_correct = 0
    while num_problems_done < TOTAL_PROBLEMS:
        print(user_prompt())
        choice = int(input("Your choice: "))
        a = generate_input()
        b = generate_input()
        c = generate_letters()
        if choice == 1:
            print(create_arithmetic_problem_prompt(a, b, "+"))
            user_answer = int(input("Your answer: "))
            true_answer = addition(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 2:
            print(create_arithmetic_problem_prompt(a, b, "-"))
            user_answer = int(input("Your answer: "))
            true_answer = subtraction(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 3:
            print(create_pythagorean_problem_prompt(a, b))
            user_answer = float(input("Your answer: "))
            true_answer = pythag(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 4:
            print(create_dna_problem_prompt(c))
            user_answer = input("Your answer: ")
            true_answer = build_complement(c)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        else:
            print("Sorry, you didn't choose a valid option!")
    print("You got " + str(num_correct) + " problems correct!")


if __name__ == "__main__":
    main()
