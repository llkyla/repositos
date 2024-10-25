import numpy as np
import math
import matplotlib.pyplot as plt

# Differential equation: y' = e^(t - y)
def f(t, y):
    return math.exp(t - y)

# Euler method implementation
def euler_method(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    return t_values, y_values

# Exact solution for comparison: y(t) = ln(e^t + e^-1)
def exact_solution(t):
    return np.log(np.exp(t) + math.exp(-1))

# Initial condition
y0 = 1
t0 = 0
t_end = 1

# Step sizes
h_values = [0.2, 0.1, 0.05]

# Store results for comparison
results = {}

# Perform Euler method with different step sizes
for h in h_values:
    t_values, y_values = euler_method(f, y0, t0, t_end, h)
    results[h] = (t_values, y_values)

# Compute exact solution for comparison
t_exact = np.linspace(t0, t_end, 100)
y_exact = exact_solution(t_exact)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_exact, y_exact, label="Exact Solution", color='black', linestyle='--')

for h in h_values:
    t_values, y_values = results[h]
    plt.plot(t_values, y_values, marker='o', label=f"Euler (h={h})")

plt.title("Euler Method vs Exact Solution")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()

# Display values for each h
for h in h_values:
    t_values, y_values = results[h]
    print(f"\nStep size h = {h}")
    print(f"{'t':>8} {'y(t)':>15}")
    for t, y in zip(t_values, y_values):
        print(f"{t:>8.3f} {y:>15.6f}")
