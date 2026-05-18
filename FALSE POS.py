import math

def run_false_position():
    print("False Position Method")

    expr = input("Enter equation f(x): ")

    def f(x):
        return eval(expr, {"x": x, "math": math})

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    tol = float(input("Enter tolerance: "))

    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Invalid interval (no sign change)")
        return

    for i in range(100):

        c = (a * fb - b * fa) / (fb - fa)
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
    run_false_position()