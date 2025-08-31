class Result:
    @staticmethod
    def get_function(n: int):
        def first_function(x, y):
            return math.sin(x)
        def second_function(x, y):
            return (x * y) / 2
        def third_function(x, y):
            return y - (2 * x) / y
        def fourth_function(x, y):
            return x + y
        def default_function(x, y):
            return 0.0

        functions = {
            1: first_function,
            2: second_function,
            3: third_function,
            4: fourth_function
        }
        return functions.get(n, default_function)

    @staticmethod
    def rk4(x0, y0, h, f):
        k1 = f(x0, y0)
        k2 = f(x0 + 0.5 * h, y0 + 0.5 * h * k1)
        k3 = f(x0 + 0.5 * h, y0 + 0.5 * h * k2)
        k4 = f(x0 + h, y0 + h * k3)
        y_next = y0 + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        return y_next

    @staticmethod
    def solveByAdams(f, epsilon, a, y_a, b):
        func = Result.get_function(f)
        h = (b - a) / 10
        x = a
        y = y_a
        history_x = [x]
        history_y = [y]
        history_f = [func(x, y)]

        while len(history_y) < 4:
            y_next = Result.rk4(x, y, h, func)
            x += h
            y = y_next
            history_x.append(x)
            history_y.append(y)
            history_f.append(func(x, y))

        while x < b:
            y_next = history_y[-1] + h * (55 * history_f[-1] - 59 * history_f[-2] + 37 * history_f[-3] - 9 * history_f[-4]) / 24
            x_next = x + h
            f_next = func(x_next, y_next)

            y_half_step_1 = Result.rk4(history_x[-1], history_y[-1], h/2, func)
            y_half_step_2 = Result.rk4(history_x[-1] + h/2, y_half_step_1, h/2, func)

            error_estimate = abs(y_half_step_2 - y_next)
            if error_estimate < epsilon:
                history_x.append(x_next)
                history_y.append(y_next)
                history_f.append(f_next)
                x = x_next
                y = y_next
                h *= min(2, (epsilon / error_estimate)**0.25)
            else:
                h *= max(0.5, (epsilon / error_estimate)**0.25)
                continue

            if x >= b:
                break
            elif x + h > b:
                h = b - x

        return history_y[-1]