#
# Complete the 'interpolate_by_newton' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY x_axis
#  2. DOUBLE_ARRAY y_axis
#  3. DOUBLE x
#
def interpolate_by_newton(f, a, b, x):
    # Выбор интерполируемой функции
    func = FunctionSet.get_function(f)

    # Количество узлов интерполяции
    n = 1

    # Предыдущее значение интерполяционного полинома
    prev_p = None

    # Итерации до достижения требуемой точности
    for _ in range(100):
        # Вычисление узлов Чебышева
        xi = _compute_chebyshev_nodes(a, b, n)

        # Список значений функции в узлах интерполяции
        y = [func(xi_i) for xi_i in xi]

        # Разности разделенных разностей
        divided_differences = _compute_divided_differences(xi, y)

        # Интерполяционный полином
        p = divided_differences[0][0]

        # Вычисление значения полинома в точке x
        for i in range(1, n):
            product = 1.0
            for j in range(i):
                product *= (x - xi[j])
            p += divided_differences[0][i] * product

        # Проверка точности
        if prev_p is not None and abs(p - prev_p) < 0.01:
            break

        prev_p = p
        n += 1

    return p


def _compute_chebyshev_nodes(a, b, n):
    return [(b + a) / 2 + (b - a) / 2 * math.cos(math.pi * (i + 0.5) / n) for i in range(n)]


def _compute_divided_differences(x_values, y_values):
    n = len(x_values)
    divided_differences = [[y_values[i] if j == 0 else 0 for j in range(n)] for i in range(n)]

    for i in range(1, n):
        for j in range(n - i):
            divided_differences[j][i] = ((divided_differences[j][i - 1] - divided_differences[j + 1][i - 1]) /
                                         (x_values[j] - x_values[i + j]))

    return divided_differences

