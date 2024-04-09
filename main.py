import math
from sympy import symbols, expand, simplify

x = symbols('x')
x0, x1, x2, x3, x4 = symbols('x0, x1, x2, x3, x4')
y0, y1, y2, y3, y4 = symbols('y0, y1, y2, y3, y4')

x_list = [x0, x1, x2, x3, x4]
y_list = [y0, y1, y2, y3, y4]

a = 12.5
b = 15.6
cond = [a, b]

val_y_list = [14.7, 21.5, 21.4, 36.0, 18.8]
val_x_list = [a]

h = (b-a) / (len(val_y_list) - 1)

for i in range(len(val_y_list) - 1):
    val_x_list.append(val_x_list[-1]+h)

def lagrange_equations_maker(index):
    equation_x = 1

    for iterations in range(0, index):
        equation_x *= (x - x_list[iterations]) / (x_list[index] - x_list[iterations])

    for iterations in range(index + 1, 5):
        equation_x *= (x - x_list[iterations]) / (x_list[index] - x_list[iterations])

    return equation_x

def lagrange(x_value):
    lagrange_equations = [lagrange_equations_maker(i) for i in range(5)]
    sub_equations = [eq.subs({x0: val_x_list[0], x1: val_x_list[1], x2: val_x_list[2], x3: val_x_list[3],
    x4: val_x_list[4]}).expand().simplify()
                    for eq in lagrange_equations]

    mult_equations = [y_val * eq for y_val, eq in zip(val_y_list, sub_equations)]

    for i, eq in enumerate(mult_equations):
        print(f"При і = {i} отримую:{eq}")

    expression = sum(mult_equations)
    print(f"\nРівняння: {expression}")
    x_expression = expression.subs(x, x_value)
    print(f"\nЗначення кінцевого рівняння при х: {x_value} : {x_expression}")
    print(f"\nПідстановка х = {val_x_list[3]} у поліном "
          f"дає:{expression.subs(x, val_x_list[3])}\n"
          f"Оригінально значення {val_y_list[3]}")

def newton(x_value):
    dy1 = []
    dy2 = []
    dy3 = []
    dy4 = []
    dyy = [val_y_list, dy1, dy2, dy3, dy4]

    for i in range(0, len(val_y_list) - 1):
        for j in range(0, len(val_y_list) - i - 1):
            dyy[i+1].append((dyy[i][j+1] - dyy[i][j]))

    max_length = max(len(val_x_list), len(val_y_list), len(dy1), len(dy2), len(dy3), len(dy4))

    print(f"Значення кінцевих різниць для функції y = f(x)")
    print("{:<8} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} ".format("x", "y", "dy1", "dy2", "dy3", "dy4",))
    print("_____________________________________________________________________________________")

    for i in range(max_length):
        x_val = "{:<8.4f}".format(val_x_list[i]) if i < len(val_x_list) else "         "
        y_val = "{:<10.4f}".format(val_y_list[i]) if i < len(val_y_list) else "         "
        dy1_val = "{:<10.4f}".format(dy1[i]) if i < len(dy1) else "          "
        dy2_val = "{:<10.4f}".format(dy2[i]) if i < len(dy2) else "          "
        dy3_val = "{:<10.4f}".format(dy3[i]) if i < len(dy3) else "          "
        dy4_val = "{:<10.4f}".format(dy4[i]) if i < len(dy4) else "          "
        print("{} | {} | {} | {} | {} | {}".format(x_val, y_val, dy1_val, dy2_val, dy3_val, dy4_val))

    eq1 = val_y_list[0]
    for i in range(0, len(dy1)):
        sub_eq = dyy[i + 1][0] / (math.pow(h, i + 1) * math.factorial(i + 1))
        for j in range(0, i + 1):
            sub_eq *= (x - val_x_list[j])
        eq1 = eq1 + sub_eq

    print(f"Отриманий поліном: {eq1}\n")
    simp_eq = simplify(eq1)
    print(f"Розкритий: {simp_eq}\n")
    print(f"Підстановка значення х2 у поліном: {eq1.subs([(x, val_x_list[2])])}\n"
          f"Початкове значення f(x2) = {val_y_list[2]}")
    print(f"Підстановка значення {x_value} у поліном: {eq1.subs([(x, x_value)])}")


    print("\n___ Друга інтерполяційна формула Ньютона ___\n")

    eq2 = val_y_list[len(val_y_list) - 1]

    for i in range(0, len(dy1)):
        sub_eq = dyy[i + 1][len(dyy[i + 1]) - 1] / (math.pow(h, i + 1) * math.factorial(i + 1))
        for j in range(0, i + 1):
            sub_eq *= (x - val_x_list[len(val_x_list) - 1 - j])
        eq2 += sub_eq

    print(f"Отриманий поліном: {eq2}")

    simp_eq2 = simplify(expand(eq2))

    print("\nРозкрита та спрощенна формула:")

    print(simp_eq2)
    print(f"Розкритий: {simp_eq2}\n")
    print(f"Підстановка значення х2 у поліном дає: {eq2.subs([(x, val_x_list[2])])}\n"
          f"Початкове значення f(x2) = {val_y_list[2]}")
    print(f"Підстановка значення {x_value} у поліном: {eq2.subs([(x, x_value)])}")
def main():
    print("Комп'ютерний практикум №4 \nВаріант №11 \nВиконав студент групи ПБ-21 \nРозумняк Руслан\n")

    x_value = 14.24

    print(f"h = {h}")
    print(f"val_x_list:", val_x_list)

    print("\n___ Інтерполяційний поліном Лагранджа ___\n")
    lagrange(x_value)
    print("\n___ Інтерполяційний поліном Ньютона ___\n")
    newton(x_value)
if __name__ == "__main__":
    main()