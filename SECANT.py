import math

def run_secant():
    print(" Secant Method ")

    expr = input("Enter equation f(x): ")

    def f(x):
        return eval(expr, {"x": x, "math": math})

    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    tol = float(input("Enter tolerance: "))

    for _ in range(100):

        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            print("Division by zero")
            return

        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(x_new - x1) < tol:
            print(f"Approximate Root: {x_new}")
            return

        x0, x1 = x1, x_new

    print(f"Approximate Root (no full convergence): {x1}")


if __name__ == "__main__":
    run_secant()