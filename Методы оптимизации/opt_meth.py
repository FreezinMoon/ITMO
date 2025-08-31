import math


def f(x):
    return math.sqrt(1 + x ** 2) - math.exp(-2 * x)


def f_prime(x):
    return x / math.sqrt(1 + x ** 2) + 2 * math.exp(-2 * x)


def f_double_prime(x):
    return -4 * math.exp(-2 * x) + 1 / math.sqrt(x ** 2 + 1) - (x ** 2) / (x ** 2 + 1) ** (3 / 2)


def bisection_method(a, b, epsilon, delta, max_steps=25):
    print("Bisection Method Iterations:")
    for step in range(max_steps):
        x1, x2 = (b + a - delta) / 2, (b + a + delta) / 2
        print(f"Step {step + 1}: a = {a:.10f}, b = {b:.10f}")
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        if (b - a) / 2 <= epsilon:
            return (a + b) / 2, f((a + b) / 2), step + 1
    return (a + b) / 2, f((a + b) / 2), max_steps


def golden_section_search(a, b, epsilon, max_steps=25):
    print("\nGolden Section Search Iterations:")
    gr = (math.sqrt(5) - 1) / 2
    current_eps = (b-a)/2
    x1 = b - gr * (b - a)
    x2 = a + gr * (b - a)
    fx1, fx2 = f(x1), f(x2)
    for step in range(max_steps):
        print(f"Step {step + 1}: a = {a:.10f}, b = {b:.10f}")
        if current_eps <= epsilon:
            break
        if fx1 <= fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = b - gr * (b - a)
            fx1 = f(x1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + gr * (b - a)
            fx2 = f(x2)
        current_eps *= gr
    return (a + b) / 2, f((a + b) / 2), step + 1


def newtons_method(a, b, epsilon, max_iterations=25):
    print("\nNewton's Method Iterations:")
    x = (a + b) / 2
    for i in range(max_iterations):
        print(f"Step {i + 1}: x = {x:.2e}, f(x) = {f(x):.2e}")
        f_prime_val = f_prime(x)
        f_double_prime_val = f_double_prime(x)
        x_next = x - f_prime_val / f_double_prime_val
        if abs(f_prime_val) <= epsilon:
            return x_next, f(x_next), i + 1
        x = x_next

    return x, f(x), max_iterations


# Parameters
a, b = 0, 1
epsilon = delta = 10 ** (-10)

# Execute the methods without duplicating output lines
bisection_method(a, b, epsilon, delta)
golden_section_search(a, b, epsilon)
newtons_method(a, b, epsilon)
