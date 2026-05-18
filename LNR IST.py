def run_least_squares():
    print(" Linear Least Squares ")

    x = list(map(float, input("Enter x: ").split()))
    y = list(map(float, input("Enter y: ").split()))

    if len(x) != len(y):
        print("Error: x and y must have same length")
        return

    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(i*i for i in x)
    sum_xy = sum(i*j for i, j in zip(x, y))

    denom = n * sum_x2 - sum_x**2
    if denom == 0:
        print("Error: division by zero")
        return

    m = (n * sum_xy - sum_x * sum_y) / denom
    c = (sum_y - m * sum_x) / n

    print(f"Best fit line: y = {m:.4f}x + {c:.4f}")


if __name__ == "__main__":
    run_least_squares()