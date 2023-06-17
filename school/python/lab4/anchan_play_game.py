"""
Project Name:   Lab 4
Module Name:    anchan_play_game.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This module runs the majority of the operational functions, such as calculations using
    subordinate functions. 
"""
import numpy
import anchan_get_stuff


def run_program():
    """When yes is chosen in main, this module activates here. This function runs the two main
    portions of the program, which is handling the phone and zip and running claculations using
    the matrices
    """
    run_phone_and_zip()
    run_matrix_operations()


def run_phone_and_zip():
    """calls for phone and zip using surbordinate functions and assigns them to local variables then
    passes those variables to the display function for operation"""
    phone_number = anchan_get_stuff.get_phone_number()
    zip_code = anchan_get_stuff.get_zip_code()
    # anchan_display.display_phone_and_zip(phone_number, zip_code) - # when display is ready
    display_phone_and_zip(phone_number, zip_code)  # to display when we are ready


def run_matrix_operations():
    """generates two matrices, assigns labels to them. displays them to the user for confirmation.
    passes the matrices to the next function to run calculations
    """
    # assigns Matrix 1 name to f-string

    matrix_1 = numpy.matrix(generate_matrices("Matrix 1"))
    # assigns Matrix 1 name to f-string
    matrix_2 = numpy.matrix(generate_matrices("Matrix 2"))
    # assigns Matrix 2 name to f-string
    # the above function calls run matrix creation and assign them to variables
    print("\nYour matrices are:")
    display_matrix("Matrix 1:", matrix_1)
    display_matrix("Matrix 2:", matrix_2)
    print(input("\nPress ENTER to continue...\t"))
    run_matrix_calculations(matrix_1, matrix_2)
    # this function takes the matrixes and runs them through a calculation such as
    # addition or multiplication


def run_matrix_calculations(matrix_1, matrix_2):
    """assigns the operator to use and then runs the calculations for the matrices.

    Args:
        matrix_1 (list): 3x3 matrix generated from user input
        matrix_2 (list): 3x3 matrix generated from user input
        operator: +, -, multiplicating (element to element), and multiplication (matrix by matrix)
    """
    operator = anchan_get_stuff.get_operator()  # assigns the operator
    matrix_results = anchan_get_stuff.get_calculation(matrix_1, matrix_2, operator)
    # above runs the calculations after operator assignment using previously generated matrics
    print_matrix_results(matrix_results)
    print_transpose(matrix_results)
    print_mean(matrix_results)


def generate_matrices(matrix_name):
    """takes information from the user, specifically integers, and then generates two lists to
    be used to generate matrices.

    Args:
        matrix_name (str): name generated during function call. Matrix 1 or Matrix 2.

    Returns:
        matrix(list): the 3x3 matrix list generated from user input, used in other functions
    """
    matrix = []
    print(f"\nPlease enter the values for {matrix_name} now.")
    print("Enters the values with the number, followed by a space. Like so: 1 2 3")
    print("Begin matrix:")
    for value in range(3):  # for look to iterate through list
        valid_row = False
        while not valid_row:
            print(f"Enter three values for row {value + 1}:\t")
            row = input().strip().split()
            # strip takes whitespace off of front and end.
            # split takes the line and seperates the line into values after each space so
            # that one line is now three different numbers instead of one string of numbers.
            if len(row) != 3:
                print("Sorry, you did not enter 3 numbers per row. Please try again.")
                continue
            try:
                row = [int(number) for number in row]
                # validates numbers and ensures whole numbers only
            except ValueError:
                print("Sorry, only whole numbers are allowed. Please try again.")
                continue
            valid_row = True
            matrix.append(row)
    return matrix


def display_matrix(matrix_name, matrix):
    """displays the matrix in proper format for user benefit

    Args:
        matrix_name (f-str): generated matrix name
        matrix (list): values in the generated matrix
    """
    matrix = matrix.tolist()
    print(f"{matrix_name}")
    for row in matrix:
        print(" ".join(f"{element}" for element in row))
        # 'join'() is a map function. join combines everything into one string. the 'f' tells the
        # string portion it is a formatted string and element is the formatted value.
        # for element in row means for each element in the row. so altogether...
        # (" ".join(f"{element}" for element in row))
        # ==
        # for each element in the row, join them into one string, format the string so there
        # is a single space between each element
        # it does this so it can print the matrix correctly with little fuss.


def print_matrix_results(matrix_results):
    """prints the matrix result from calculations for user benefit


    Args:
        matrix_results (list): results from calculation run on matrixes 1 and 2
    """
    matrix_results = matrix_results.tolist()
    print("The results for your selected operation are:\n")
    for row in matrix_results:
        print(" ".join(f"{element}" for element in row))
    print(input("\nPress ENTER to continue...\t"))  # pause for user


def print_transpose(matrix_results):
    """This function prints the transpose of the matrix.

    Args:
        matrix_results (list): results fromn calculations
    """
    matrix_transpose = numpy.transpose(matrix_results)
    matrix_transpose = matrix_transpose.tolist()
    # numpy requires this to play nice. I guess lists are different than standard lists or
    # something, least that's what I read when I looked it up a while back. I think.
    # transpose() is a built-in numpy function, ignore the voodoo
    print("The matrix transpose is:\n")
    for row in matrix_transpose:
        print(" ".join(f"{element}" for element in row))
    print(input("\nPress ENTER to continue...\t"))  # pause for user


def print_mean(matrix_results):
    """This function prints the mean of the matrix.

    Args:
        matrix_results (list): results fromn calculations
    """
    matrix_mean = numpy.mean(matrix_results)
    # mean() is a built-in numpy function, ignore the voodoo
    matrix_mean = matrix_mean.tolist()
    # numpy requires this to play nice. I guess lists are different than standard lists or
    # something, least that's what I read when I looked it up a while back. I think.
    print("The mean is:", matrix_mean)
    print(input("\nPress ENTER to continue...\t"))  # pause for user


def display_phone_and_zip(phone_number, zip_code):
    """function used to generate display messages for phone and zip funcs"""
    print("\nYou have successfully enter your Phone Number and Zip Code:")
    print("Phone Number:\t", phone_number)
    print("Zip Code:\t", zip_code)
    print(input("Press ENTER to continue...\t"))


# Unit Testing
# def test_matrix_generation():
#     matrix_1 = generate_matrices("Matrix 1")  # assigns Matrix 1 name to f-string
#     matrix_2 = generate_matrices("Matrix 2")  # assigns Matrix 2 name to f-string
#     display_matrix(matrix_1, "Matrix 1:\n")
#     display_matrix(matrix_2, "Matrix 2:\n")
#
# run_matrix_operations()
# run_program()
