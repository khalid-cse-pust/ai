import numpy as np

# Example function: f(x) = x^2 - 4x + 4
def f(x):
    return x**2 - 4*x + 4

# Derivative of the function: f'(x) = 2x - 4
def df(x):
    return 2*x - 4

# Gradient Descent algorithm
def gradient_descent(start, learning_rate=0.1, iterations=50, tolerance=1e-6):
    x = start
    for i in range(iterations):
        grad = df(x)
        x_new = x - learning_rate * grad
        # Stop if gradient is small (converged)
        if abs(x_new - x) < tolerance:
            break
        x = x_new
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}")
    return x, f(x)

# --- Run Gradient Descent ---
start_point = 0  # initial guess
learning_rate = 0.1
x_min, f_min = gradient_descent(start_point, learning_rate)

print("\nMinimum value found at x =", x_min)
print("f(x) =", f_min)
