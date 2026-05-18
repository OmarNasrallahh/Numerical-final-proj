def run_jacobi():
    print("Jacobi Method")

    n = int(input("Enter number of variables: "))

    print("Enter matrix A row by row:")
    A = []
    for i in range(n):
        A.append(list(map(float, input(f"Row {i+1}: ").split())))

    b = list(map(float, input("Enter b values: ").split()))

    x = [0.0] * n
    tol = float(input("Enter tolerance: "))
    max_iter = int(input("Enter max iterations: "))

    for k in range(max_iter):
        x_new = [0.0] * n

        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            x_new[i] = (b[i] - s) / A[i][i]

        error = max(abs(x_new[i] - x[i]) for i in range(n))

        x = x_new

        print(f"Iteration {k+1}: {x}")

        if error < tol:
            print("Converged!")
            break


if __name__ == "__main__":
    run_jacobi()