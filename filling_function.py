__author__ = 'lyndsay.beaver'
import re, string, itertools


def solve(rawFormula):
    """
    rawFormula = "SEND + MORE = MONEY"
    Test all possible translations between Character string and Numbered string
    Return the Solution to the puzzle or None if no solution is found.
    """

    for formula in fill_in(rawFormula):
        if valid(formula):
            return formula
        return None

def fill_in(rawFormula):
    """
    Generatate all possible translations between Character string and Numbered string
    """
    letters = ''.join(set(re.findall('[A-Z]', rawFormula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield rawFormula.translate(table)


def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    1/0 = 1 --> ERROR, Dividing by Zero
    """

    try:
        return not re.search(r'\b0[0-9]', formula) and eval((formula) is True
    #except ArithmeticError:
        #return False
    except:
        return False


print(solve('SEND + MORE == MONEY'))
