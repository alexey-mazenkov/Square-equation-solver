# coding=utf-8
# Square equation solver v1.
# Developer: Mazenkov A.

import localization as lc

# Square equation formula.
print(lc.formula)

while True:

    a = int(input(lc.a_coeff))
    b = int(input(lc.b_coeff))
    c = int(input(lc.c_coeff))

    # Calculate the discriminant.
    d = (b ** 2) + (-4 * a * c)

    # Extracting the roots of an equation.
    if d >= 0:
        x = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(lc.x, x, lc.x2, x2)
    else:
        print(lc.error)

    # Whether to continue the cycle.
    # If yes = continue, if no = break.
    end = input(lc.cont)
    if end == 'no':
        break

print(lc.thanks)