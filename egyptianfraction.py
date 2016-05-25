#egyptianfraction
#by Paul Chifita

from math import ceil
from fractions import Fraction

def main():
    num = eval(input('Enter numerator: '))
    den = eval(input('Enter denominator: '))
    
    solution = []
    fraction = Fraction(int(num), int(den))
    while fraction < 1:
        if fraction.numerator == 1:
            solution.append(fraction)
            break
        x = Fraction(1, int(ceil(float((fraction.denominator) / (fraction.numerator)))))

        fraction = fraction - x
        solution.append(x)
    print(solution)

main()
