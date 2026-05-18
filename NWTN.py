import math


def newton(f, x0, tol=1e-6, max_iter=100):
    x = x0

    for i in range(max_iter):

        fx = f(x)
        dfx = (f(x + 1e-8) - f(x - 1e-8)) / (2e-8)

        if abs(dfx) < 1e-14:
            return "Derivative too small"

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return "No convergence"


def run_newton():
    print("--- Newton Method ---")

    expr = input("Enter f(x): ")

    def f(x):
        return eval(expr, {"x": x, "math": math})

    x0 = float(input("x0: "))
    tol = float(input("tolerance: "))

    print(newton(f, x0, tol))


if __name__ == "__main__":
    run_newton()