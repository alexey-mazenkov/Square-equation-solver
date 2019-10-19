# coding=utf-8
# Square equation solver v0.1
# Developer: Mazenkov A.

# Square equation formula.
print('Формула квадратного уравнения: ax^2 + bx + c = 0')

while True:

    a = int(input('Введите коэффициент a : '))
    b = int(input('Введите коэффициент b : '))
    c = int(input('Введите коэффициент c : '))

    # Calculate the discriminant.
    d = (b ** 2) + (4 * a * c)

    # Extracting the roots of an equation.
    if d >= 0:
        x = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        print('x1 =', x, '\nx2 =', x2)

    else:
        print('Корней нет')

    # Whether to continue the cycle.
    # If yes = continue, if no = break.
    end = input('Решить ещё одно уравнение? (yes/no): ')
    if end == 'no':
        break