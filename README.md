# Numerical Final Project
This project contains Python implementations of common numerical methods for root finding, solving linear systems, and fitting a line using least squares.

## Included methods
- `BISEC.py` — Bisection method
- `FALSE POS.py` — False Position (Regula Falsi) method
- `NWTN.py` — Newton-Raphson method (with numerical derivative)
- `SECANT.py` — Secant method
- `JACOBI.py` — Jacobi iterative method for linear systems
- `GAUSS.py` — Gauss-Seidel iterative method for linear systems
- `LNR IST.py` — Linear least squares line fitting

## Requirements
- Python 3.x

No external libraries are required; all scripts use Python built-ins and `math`.

## How to run
From the project folder, run any script:

```powershell
python "BISEC.py"
python "FALSE POS.py"
python "NWTN.py"
python "SECANT.py"
python "JACOBI.py"
python "GAUSS.py"
python "LNR IST.py"
```

Each program is interactive and will ask for inputs (equation, interval, tolerance, matrix values, etc.) depending on the selected method.

## Notes
- For equation-based scripts, enter expressions using `x` and `math` functions (example: `x**3 - x - 2`, `math.sin(x) - 0.5`).
- Root-finding interval methods (Bisection and False Position) require a valid interval with a sign change.
- `NWTN.py` approximates the derivative numerically.
