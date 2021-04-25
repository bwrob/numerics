import types
from math import sin

from utils import debugging, RootFindingData


# Newton Method
# We are considering only single multiplicity isolated real roots
# 1. Find a suspect interval
# 2. Find a x_0 point "close" to the root
# 3. Iterate x_{n+1} = x_n - f(x_n)/f'(x_n)
# 4. x^* = Lim x_n
@debugging()
def root_newton(debug, sleep, f, start_point, epsilon, h=0.000001):
    max_iter = 100000
    i = 0
    points = []
    current_point = start_point
    while i < max_iter:
        i += 1
        value = f(current_point)
        if debug:
            points.append((current_point, value))
        value_h = f(current_point + h)
        next_point = current_point + h * (1 - value_h / (value_h - value))
        if abs(next_point - current_point) < epsilon:
            return RootFindingData(value=next_point, iteration_points=points, iteration_no=i)
        else:
            current_point = next_point
    return RootFindingData(value=None, iteration_points=points, iteration_no=i)


@debugging()
def root_secant(debug, sleep, f, point_zero, point_one, epsilon):
    max_iter = 100000
    i = 0
    points = []
    while i < max_iter:
        i += 1
        value_zero = f(point_zero)
        value_one = f(point_one)
        if debug:
            points.append((point_zero, value_zero))
        point_next = point_one - value_one * (point_one - point_zero) / (value_one - value_zero)
        if abs(point_next - point_one) < epsilon:
            return RootFindingData(value=point_next, iteration_points=points, iteration_no=i)
        else:
            point_zero, point_one = point_one, point_next
    return RootFindingData(value=None, iteration_points=points, iteration_no=i)


@debugging()
def root_bisection(debug, sleep, f, a, b, epsilon, weighted):
    i = 0
    points = []
    max_iter = 10000
    y_1, y_2 = f(a), f(b)
    check = y_1 * y_2
    if check == 0:
        return a if y_1 == 0 else b
    if check > 0:
        raise Exception("nope")
    while i < max_iter:
        i += 1
        y_1, y_2 = f(a), f(b)
        w_1, w_2 = (abs(y_1) / (abs(y_1) + abs(y_2)), abs(y_2) / (abs(y_1) + abs(y_2))) if weighted else (1 / 2, 1 / 2)
        midpoint = w_1 * a + w_2 * b
        y_3 = f(midpoint)
        if debug:
            points.append((midpoint, y_3))
        if abs(a - b) < epsilon:
            return RootFindingData(value=midpoint, iteration_points=points, iteration_no=i)
        if y_1 * y_3 < 0:
            a, b = a, midpoint
        else:
            a, b = b, midpoint
    return RootFindingData(value=None, iteration_points=points, iteration_no=i)


if __name__ == '__main__':
    g = (lambda x: sin(x))
    accuracy = 0.00001

    result = root_newton(g, 0.5, accuracy)
    print("result Newton: {}".format(result))

    result = root_secant(g, 3.0, 3.5, accuracy)
    print("result secant: {}".format(result))

    result = root_bisection(g, -0.1, 0.2, accuracy, weighted=False)
    print("result bisection: {}".format(result))
