def iterate_approximations(funcs, curr_approx, params):
    return [x - f(curr_approx) * p for x, f, p in zip(curr_approx, funcs, params)]


def is_converged(next_approx, curr_approx, epsilon):
    return all(abs(n - c) < epsilon for n, c in zip(next_approx, curr_approx))


def update_parameters(funcs, next_approx, curr_approx, params):
    return [-p if abs(f(next_approx)) >= abs(f(curr_approx)) else p for f, p in zip(funcs, params)]


def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    epsilon, max_iter = 5e-6, 10000
    funcs = get_functions(system_id)
    params = [0.001] * number_of_unknowns

    for _ in range(max_iter):
        next_approx = iterate_approximations(funcs, initial_approximations, params)
        if is_converged(next_approx, initial_approximations, epsilon):
            return [round(x, 5) for x in next_approx]
        params = update_parameters(funcs, next_approx, initial_approximations, params)
        initial_approximations = next_approx
    raise ValueError("Non-convergence within max iterations")