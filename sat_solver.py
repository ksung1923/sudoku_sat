
# Format for Output Variables
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


# Description: Create boolean variable
# Output: 1 variable that represents a single number in a single box in sudoku possibility 
def sudoku_var(row, col, num): 
    #return  str(row) + '-' +  str(col) + str(num).translate(SUB)
    return [row, col, num]


# Description: Creates boolean variable for each number 1-9 for a box 
# Output: 9 variables that represent 1 through 9 possible output for a specific row, col
def sudoku_box_vars(row, col):
    return [sudoku_var(row, col, num) for num in range(1,10)]


# Description: Create all boolean variables for single row 
# Output: 9 variables over 9 col = 81 variables outputted 
def row_vars (row): 
    return [sudoku_box_vars(row, col) for col in range(0,9)]


# Description: Create all boolean variables for all rows in sukodu grid
# Output: 81 row_vars * 9 rows = 729 boolean variables 
def grid_vars ():
    return [row_vars(row) for row in range(0,9)]


def and_vars(variables):
    return ["AND"] + variables

def or_vars(ands):
    return ["OR"] + ands

def solve(formula):
    # get a variable to test
    test = formula[1][1]

    # set that variable to a value (replace variable in the formula
    for and_vars in formula[1:]: 
        for variable in and_vars[1:]: 
            if variable == test: 
                variable = True
    # simplify formula
    # solve the new formula


ands = and_vars([[0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 0, 6], [0, 0, 7], [0, 0, 8], [0, 0, 9]])

example_formula = or_vars([ands, ands, ands])

[print(and_statement) for and_statement in example_formula]

solve(example_formula)

[print(and_statement) for and_statement in example_formula]
