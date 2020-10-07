def arithmetic_arranger(problems, answers=False):

    # check if there isn't more than 5 problems given
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # set default variables
    operators = ('+', '-')
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""

    #loop through given problems
    for n, problem in enumerate(problems):
        # set default variables of every problem
        a, operator, b = problem.split()
        
        # get lengh of every digit
        len_a = len(a)
        len_b = len(b)

        # check if given operator is correct
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."

        # check if given strings are digit
        if a.isdigit() == False or b.isdigit() == False:
            return "Error: Numbers must only contain digits."

        # check if lengh of every number is correct
        if len_a > 4 or len_b > 4:
            return "Error: Numbers cannot be more than four digits."

        # do mathematics for given operator
        if operator == "+":
            answer = int(a) + int(b)

        else:
            answer = int(a) - int(b)

        # handling spaces in output
        spaces = max(len_a, len_b) + 2

        additional_spaces = '    '

        # formatting output
        row1 += a.rjust(spaces)
        row2 += operator + b.rjust(spaces-1)
        row3 += "-" * spaces
        row4 += str(answer).rjust(spaces)

        # handle spaces between each column
        if n < len(problems) - 1:
                row1 += additional_spaces
                row2 += additional_spaces
                row3 += additional_spaces
                row4 += additional_spaces

        # if answers are wanted, show them
        if answers == True:
            arranged = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4

        # if not, return result without them
        else:
            arranged = row1 + "\n" + row2 + "\n" + row3
        
    return arranged