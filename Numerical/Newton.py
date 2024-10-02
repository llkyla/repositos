import math

# Function f(x) 
def f(x):
    return math.log(x) - 1

# Function f(x) 
def f_prime(x):
    return 1 / x

# Newton Method
def newton(x0, tol=1e-3, max_iter=100):
    x = x0
    iteration = 0
    results = []

    while iteration < max_iter:
        x_next = x - f(x) / f_prime(x)
        results.append((iteration, x, x_next, f(x_next)))
        
        if abs(x_next - x) < tol:
            return results, x_next, iteration
        
        x = x_next
        iteration += 1

    return results, x_next, iteration

# Initial guess
x0 = 2.5
results, root, num_iterations = newton(x0)

# Print Table
print(f"{'n':<3} | {'x_n':<10} | {'x_{n+1}':<10} | {'f(x_{n+1})':<15}")
print("-" * 40)
for result in results:
    n, x_n, x_next, fx_next = result
    print(f"{n:<3} | {x_n:<10.4f} | {x_next:<10.4f} | {fx_next:<15.6f}")

# Print Results
print(f"\nNumber of iterations: {num_iterations}")
print(f"Root found: {root:.4f}")
