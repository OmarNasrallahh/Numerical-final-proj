import math

def run_bisection():
    print(" Bisection Method ")

    expr = input("Enter equation f(x): ")

    def f(x):
        return eval(expr, {"x": x, "math": math})

    a = float(input("Enter start of interval (a): "))
    b = float(input("Enter end of interval (b): "))
    tol = float(input("Enter tolerance: "))

    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Error: interval must have opposite signs.")
        return

    while (b - a) / 2 > tol:

        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print(f"Approximate Root: {c}")


if __name__ == "__main__":
    run_bisection()