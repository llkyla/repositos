import math

# Function f(x)
def f(x):
    return math.log(x) - 1

# Secant Method
def secant_method(x0, x1, tol=1e-3, max_iter=100):
    iterations = []
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        
        # Secant method formula
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        
        # Store iteration results
        iterations.append((i, x0, x1, f1))
        
        # Check for convergence
        if abs(f2) < tol:
            iterations.append((i + 1, x1, x2, f2))
            return x2, iterations
        
        # Update for next iteration
        x0, x1 = x1, x2
    
    # If max iterations reached
    return x1, iterations

# Initial guesses
x0 = 2
x1 = 3

# Find the root
root, iter_results = secant_method(x0, x1)


# Print Table
print(" ")
print(f"{'n':<5} {'x_n':<15} {'x_{n+1}':<15} {'f(x_{n+1})':<15}")
print("-" * 48)
for n, xn, xn1, fxn1 in iter_results:
    print(f"{n:<5} {xn:<15.6f} {xn1:<15.6f} {fxn1:<15.6f}")

# Print Results
print(" ")

print(f"Number of iterations: {len(iter_results)}")
print(f"Root found: {root:.6f}")
