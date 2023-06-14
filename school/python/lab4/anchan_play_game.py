"""
Project Name:   Lab 4
Module Name:    anchan_play_game.py
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import numpy
import anchan_get_stuff


def run_program():
    run_zip_and_code()
    run_matrix_operations()


def run_zip_and_code():
    phone_number = anchan_get_stuff.get_phone_number()
    zip_code = anchan_get_stuff.get_zip_code()
    # anchan_display.display_phone_and_zip(phone_number, zip_code) - # when display is ready
    display_phone_and_zip(phone_number, zip_code)  # to display when we are ready


def run_matrix_operations():
    matrix_1 = numpy.matrix(generate_matrices("Matrix 1"))
    matrix_2 = numpy.matrix(generate_matrices("Matrix 2"))
    # the above functions run matrix creation and assign them to variables
    print("\nYour matrices are:")
    display_matrix("Matrix 1:", matrix_1)
    display_matrix("Matrix 2:", matrix_2)
    print(input("\nPress ENTER to continue...\t"))
    run_matrix_calculations(matrix_1, matrix_2)
    # this function takes the matrixes and runs them through a calculation such as
    # addition or multiplication


def run_matrix_calculations(matrix_1, matrix_2):
    operator = anchan_get_stuff.get_operator()
    matrix_results = anchan_get_stuff.get_calculation(matrix_1, matrix_2, operator)
    print_matrix_results(matrix_results)
    print_transpose(matrix_results)
    print_mean(matrix_results)


def generate_matrices(matrix_name):
    matrix = []
    print(f"\nPlease enter the values for {matrix_name} now.")
    print("Enters the values with the number, followed by a space. Like so: 1 2 3")
    print("Begin matrix:")
    for value in range(3):  # for look to iterate through list
        valid_row = False
        while not valid_row:
            print(f"Enter three values for row {value + 1}:\t")
            row = input().strip().split()
            # strip takes whitespace off of front and end
            # split takes the line and seperates the line into values after each space so
            ## that one line is now three different numbers instead of one string of numbers
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
    # print("Final matrix (for testing purposes):")
    # for row in matrix:
    #     print(*row)
    return matrix


def display_matrix(matrix_name, matrix):
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
    matrix_results = matrix_results.tolist()
    print("The results for your selected operation are:\n")
    for row in matrix_results:
        print(" ".join(f"{element}" for element in row))
    print(input("\nPress ENTER to continue...\t"))


def print_transpose(matrix_results):
    matrix_transpose = numpy.transpose(matrix_results)
    matrix_transpose = matrix_transpose.tolist()
    # transpose() is a built-in numpy function, ignore the voodoo
    print("The matrix transpose is:\n")
    for row in matrix_transpose:
        print(" ".join(f"{element}" for element in row))
    print(input("\nPress ENTER to continue...\t"))


def print_mean(matrix_results):
    matrix_mean = numpy.mean(matrix_results)
    # mean() is a built-in numpy function, ignore the voodoo
    matrix_mean = matrix_mean.tolist()
    print("The mean is:", matrix_mean)
    print(input("\nPress ENTER to continue...\t"))


def display_phone_and_zip(phone_number, zip_code):  # to display when we are ready
    print("\nYou have successfully enter your Phone Number and Zip Code:")
    print("Phone Number:\t", phone_number)
    print("Zip Code:\t", zip_code)
    print(input("Press ENTER to continue...\t"))


# Testing
def test_matrix_generation():
    matrix_1 = generate_matrices("Matrix 1")
    matrix_2 = generate_matrices("Matrix 2")
    display_matrix(matrix_1, "Matrix 1:\n")
    display_matrix(matrix_2, "Matrix 2:\n")


# run_program()
run_matrix_operations()
