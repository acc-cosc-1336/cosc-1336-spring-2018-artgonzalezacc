def sample_function(value):
    '''Return value given'''
    return value

def valid_letter_grade(letter_grade):
    '''
    Given a letter grade determine if it's in the range A, B, C, D, F, a, b, c, d, f
    :param letter_grade: A letter grade
    :return: True boolean expression if letter grade in range False otherwise.
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    while letter_grade == 'A' or letter_grade == 'a' or letter_grade == 'B' or letter_grade == 'b' or \
            letter_grade == 'C' or letter_grade == 'c' or letter_grade == 'D' or letter_grade == 'd' or\
            letter_grade == 'F' or letter_grade == 'f':
        return True
    else:
        return False

def get_credit_points(letter_grade):
    '''
    Given a letter grade return the credit points associated with that grade.
    IN BLACKBOARD: SEE TABLE IN HOMEWORK 4 ASSIGNMENT.
    :param letter_grade: One letter grade
    :return: a whole number representing the credit points
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''

    if letter_grade == 'A' or letter_grade == 'a':
        return 4
    elif letter_grade == 'B' or letter_grade == 'b':
        return 3
    elif letter_grade == 'C' or letter_grade == 'c':
        return 2
    elif letter_grade == 'D' or letter_grade == 'd':
        return 1
    else:
        return 0

def get_grade_points(credit_hours, credit_points):
    '''
    Return grade points given credit hours and credit points.

    :param credit_hours: Credit hours for a class
    :param credit_points: Credit points for a class
    :return: Total grade points for a class
    '''

    return credit_hours * credit_points

def get_grade_point_average(credit_hours, grade_points):
    '''
    Returns grade point average as a decimal value (float)
    :param credit_hours: Total credit hours for a student.
    :param grade_points: Total grade points for a student.
    :return: The grade point average for a student
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''

    return grade_points / credit_hours
