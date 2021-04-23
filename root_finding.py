from math import sin


def derivative(f, x, h=0.001):
    return (f(x + h) - f(x - h)) / (2 * h)


# Newton Method
# We are considering only single multiplicity isolated real roots
# 1. Find a suspect interval
# 2. Find a x_0 point "close" to the root
# 3. Iterate x_{n+1} = x_n - f(x_n)/f'(x_n)
# 4. x^* = Lim x_n
def root_newton(f, start_point, epsilon, h=0.000001, debug=False):
    max_iter = 100000
    i = 0
    current_point = start_point
    while i < max_iter:
        i += 1
        value = f(current_point)
        value_h = f(current_point + h)
        if debug:
            print("step {}:\t{}, {}, {}".format(i, current_point, value, value_h))
        next_point = current_point + h * (1 - value_h / (value_h - value))
        if abs(next_point - current_point) < epsilon:
            print(i)
            return next_point
        else:
            current_point = next_point
    return None


def root_secant(f, point_zero, point_one, epsilon):
    max_iter = 100000
    i = 0
    while i < max_iter:
        i += 1
        value_zero = f(point_zero)
        value_one = f(point_one)
        point_next = point_one - value_one * (point_one - point_zero) / (value_one - value_zero)
        if abs(point_next - point_one) < epsilon:
            print(i)
            return point_next
        else:
            point_zero, point_one = point_one, point_next
    return None


def root_bisection(f, a, b, epsilon=0.0001, weighted=False):
    i = 0
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
        w_1, w_2 = (abs(y_1) / (abs(y_1) + abs(y_2)), abs(y_2) / (abs(y_1) + abs(y_2)) ) if weighted else (1 / 2, 1 / 2)
        midpoint = w_1 * a + w_2 * b
        y_3 = f(midpoint)
        if abs(a - b) < epsilon:
            print(i)
            return midpoint
        if y_1 * y_3 < 0:
            a, b = a, midpoint
        else:
            a, b = b, midpoint
    return None


g = (lambda x: sin(x))
accuracy = 0.00001

result = root_newton(g, 0.5, accuracy)
print("result Newton: {}".format(result))

result = root_secant(g, 3.0, 3.5, accuracy)
print("result secant: {}".format(result))

result = root_bisection(g, -0.1, 0.2, accuracy, weighted=False)
print("result secant: {}".format(result))
