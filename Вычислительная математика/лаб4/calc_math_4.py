class Result:
    error_message = ""
    has_discontinuity = False

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
        return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x: float):
        return math.log(x)

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def calculate_integral(a, b, f, epsilon):
        # Write your code here
        Result.eps = epsilon
        func = Result.get_function(f)
        n = 10  # Initial number of partitions
        integral_prev = 0
        try:
            while True:
                h = (b - a) / n
                x_i = [a + i * h for i in range(n + 1)]
                integral_current = h * (func(a) + func(b)) / 2
                for i in range(1, n):
                    integral_current += h * func(x_i[i])

                if abs(integral_current - integral_prev) < epsilon:
                    return integral_current
                else:
                    integral_prev = integral_current
                    n *= 2  # Double the number of partitions for better accuracy

        except ValueError:
            Result.has_discontinuity = True
            Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
            return
        except ZeroDivisionError:
            Result.has_discontinuity = True
            Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
            return
