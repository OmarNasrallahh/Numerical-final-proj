def run_gauss_seidel():
    print("Gauss-Seidel Method")

    n = int(input("Enter number of variables: "))

    A = []
    for i in range(n):
        A.append(list(map(float, input(f"Row {i+1}: ").split())))

    b = list(map(float, input("Enter b values: ").split()))

    x = [0.0] * n

    tol = float(input("Enter tolerance: "))
    max_iter = int(input("Enter max iterations: "))

    for k in range(max_iter):

        x_old = x[:]

        for i in range(n):
            s = 0

            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]   # لاحظ هنا Gauss-Seidel يستخدم x updated

            x[i] = (b[i] - s) / A[i][i]

        print(f"Iteration {k+1}: {x}")

        error = max(abs(x[i] - x_old[i]) for i in range(n))

        if error < tol:
            print("Converged!")
            break

    print("Final solution:", x)


if __name__ == "__main__":
    run_gauss_seidel()