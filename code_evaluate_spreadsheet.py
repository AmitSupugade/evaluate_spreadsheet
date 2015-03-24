
# =============================================================================
#
#Implemented by Amit Supugade
#
# =============================================================================

#Import re library and initialization 
import re


#Function to convert String to Column Number
def string_to_column(s):
    num = 0
    s = s.upper()
    length = len(s)
    for i in range(0, length):
        num += (ord(s[i]) - 64) * (26 ** (length - i - 1))
    return num-1



#Function to convert Column number to String
def column_to_string(n):
    s = ''
    while(n>0):
        temp = (n-1)%26
        s = chr(65+temp) + s
        n = (n-1)/26
    return s



#Function to seperate characters from numbers in a string
def int_seperator(s):
    p = re.compile('([a-z A-Z]+)([0-9]+)')
    m = p.match(s)
    items = m.groups()
    return items



#Function to remove spaces from string
def remove_space(s):
    if is_number(s):
        return s
    else:
        return s.replace(' ', '')



#Function to decide the operator present in the String
def find_operator(s):
    o = "+-*/"
    for ch in o:
        if s.find(ch) != -1:
            return ch
    return -1



#Function to convert string in to index
def alphanumeric_to_index(s):
    index = int_seperator(s)
    col = string_to_column(index[0])
    row = int(index[1]) - 1
    return (row, col)



#Function to convert index in to string representation
def index_to_alphanumeric(index):
    return column_to_string(index[1]+1) + str(index[0]+1)



#Function to calculate the value by arithmatic operation
def calculate_value(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return float(num1) / num2





#Function to check for ReferenceError
def is_referenceError(index, limit):
    if index[0] >= limit[0] or index[1] >= limit[1]:
        raise ReferenceError




#Function to check for ValueError
def is_valueError(value, cells):
    if cells.has_key(value):
        cells = {}
        raise ValueError
  



#Function to convert string of digits in to number
def string_to_numeric(s):
    if s.find('.') == -1:
        return int(s)
    else:
        return float(s)



#Function to determine whether string is a numeric or not
def is_numeric(s):
    if s[0] == '=':
        return False
    elif s.isdigit():
        return True
    elif s.find('.') != -1:
        return True
    else:
        return False




#Function to determine whether variable is a number or not
def is_number(n):
    if isinstance(n, int):
        return True
    elif isinstance(n, float):
        return True
    else:
        return False




#Function to get or calculate value from string
def evaluate_string(s, m, current, limit, cells):
    if is_numeric(s):
        answer = string_to_numeric(s)
    else:
        is_valueError(s, cells)
        cells[index_to_alphanumeric(current)] = 1
        index = alphanumeric_to_index(s)
        answer = evaluate_cell(m, index, limit, cells)
        cells.pop(index_to_alphanumeric(current))
    return answer




#Calculates and returns the value at current cell
def evaluate_cell(m, current, limit, cells):
    is_referenceError(current, limit)
    cell_value = remove_space(m[current[0]][current[1]])
    if is_number(cell_value):
        return cell_value
    if is_numeric(cell_value):
        return string_to_numeric(cell_value)

    cell_value = cell_value[1:]
    op = find_operator(cell_value)

    if op == -1:
        return evaluate_string(cell_value, m, current, limit, cells)
    else:
        values = cell_value.split(op)
        n1 = evaluate_string(values[0], m, current, limit, cells)
        n2 = evaluate_string(values[1], m, current, limit, cells)
        return calculate_value(n1, n2, op)



    
#Function to calculate the values at every cell in a matrix
def evaluate(m):
    cells = {}
    limit = (len(m), len(m[0]))
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            current = (i, j)
            m[i][j] = evaluate_cell(m, current, limit, cells)
    return m


# =============================================================================
#
#END
#
# =============================================================================


########################################################################
#Tests-

m1 = [
    [1, "2"],
    ["3", 4]
]

solution1 = [
    [1, 2],
    [3, 4]
]

m2 = [
    [1, "=A1+1"],
    [3, "=3+ 3.5"]
]

solution2 = [
    [1, 2],
    [3, 6.5]
]

m3 = [
    [1,     "=A1+1", "=A1 + B1"],
    ["=B1", "13.5",     "=C1 + B2"]
]

solution3 = [
    [1, 2, 3],
    [2, 13.5, 16.5]
]

m4 = [
    [1,         "=C1 + 2"],
    ["=B1 + 1", "=A2 + 1"]
]

m5 = [
    ["=B1 + 1", "=A1 + 1"]
]

m6 =[
    [1,     "=B2+1", "=A1 +1"],
    ["=B2+5", "=C1+ 3.5",     "=C1 + B2"]
]

solution6 = [
    [1, 6.5, 2],
    [10.5, 5.5, 7.5]
]

m7 = [
    [1,     "=B2+1", "=A1 +1"],
    ["=B1+5", "=A2+ 3",     "=C1 + B2"]
]

m8 = [
    [1,     "=A2+10", "=A1 +1"],
    ["=C2", "=C1 + 3",     "=C1 + B2"]
]

solution8 = [
    [1, 17, 2],
    [7, 5, 7]
]

m9 = [
    [1.0,     "=A2-1", "=A1 + 10"],
    ["=C2", "=C1/ 3",     "=C1 * B2"]
]

solution9 = [
    [1.0, 39.33333333333333, 11.0],
    [40.33333333333333, 3.6666666666666665, 40.33333333333333]
]

m10 = [
    [1,     "=A1/4", "=A1 * B1"],
    ["=B1", "= 4.5 - 1",     "=C1 + B2"],
    ["=C3 / 3", 12.9, "=C2-C1"]
]

solution10 = [
    [1, 0.25, 0.25],
    [0.25, 3.5, 3.75],
    [1.1666666666666667, 12.9, 3.5]
]

def validate(proposed, actual):
    if proposed is None:
        print "Oops! Looks like your proposed result is None."
        return False
    proposed_items = [item for sublist in proposed for item in sublist]
    actual_items = [item for sublist in actual for item in sublist]
    if len(proposed_items) != len(actual_items):
        print "Oops! There don't seem to be the same number of elements."
        return False
    if proposed_items != actual_items:
        print "Oops! Looks like your proposed solution is not right..."
        return False
    return True


if __name__ == '__main__':

    # The number of test cases that are correct
    correct = 0

    print "Test 1."
    if validate(evaluate(m1), solution1):
        print "    OK."
        correct += 1
    
    print "Test 2."
    if validate(evaluate(m2), solution2):
        print "    OK."
        correct += 1
    
    print "Test 3."
    if validate(evaluate(m3), solution3):
        print "    OK."
        correct += 1
    
    print "Test 4."
    try:
        evaluate(m4)
    except ReferenceError:
        print "    OK."
        correct += 1
    
    print "Test 5."
    try:
        evaluate(m5)
    except ValueError:
        print "    OK."
        correct += 1
    
    print "Test 6."
    if validate(evaluate(m6), solution6):
        print "    OK."
        correct += 1
    
    print "Test 7."
    try:
        evaluate(m7)
    except ValueError:
        print "    OK."
        correct += 1
    
    print "Test 8."
    if validate(evaluate(m8), solution8):
        print "    OK."
        correct += 1
    
    print "Test 9."
    if validate(evaluate(m9), solution9):
        print "    OK."
        correct += 1

    print "Test 10."
    if validate(evaluate(m10), solution10):
        print "    OK."
        correct += 1
        
    print "------------------------------------------------------"
    print "You got {} out of 10 correct.".format(correct)

########################################################################
