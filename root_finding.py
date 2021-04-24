import types
from math import sin

from decorators import value_only


# Newton Method
# We are considering only single multiplicity isolated real roots
# 1. Find a suspect interval
# 2. Find a x_0 point "close" to the root
# 3. Iterate x_{n+1} = x_n - f(x_n)/f'(x_n)
# 4. x^* = Lim x_n
@value_only
def root_newton(f, start_point, epsilon, debug, h=0.000001):
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
            output = types.SimpleNamespace()
            output.value = next_point
            output.points = points
            return output
        else:
            current_point = next_point
    output = types.SimpleNamespace()
    output.points = points
    return output


@value_only
def root_secant(f, point_zero, point_one, epsilon, debug):
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
            output = types.SimpleNamespace()
            output.value = point_next
            output.points = points
            return output
        else:
            point_zero, point_one = point_one, point_next
    output = types.SimpleNamespace()
    output.points = points
    return output


@value_only
def root_bisection(f, a, b, epsilon, weighted, debug):
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
            output = types.SimpleNamespace()
            output.value = midpoint
            output.points = points
            return output
        if y_1 * y_3 < 0:
            a, b = a, midpoint
        else:
            a, b = b, midpoint
    output = types.SimpleNamespace()
    output.points = points
    return output


if __name__ == '__main__':
    g = (lambda x: sin(x))
    accuracy = 0.00001

    result = root_newton(g, 0.5, accuracy)
    print("result Newton: {}".format(result))

    result = root_secant(g, 3.0, 3.5, accuracy)
    print("result secant: {}".format(result))

    result = root_bisection(g, -0.1, 0.2, accuracy, weighted=False)
    print("result bisection: {}".format(result))
