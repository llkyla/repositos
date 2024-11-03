import numpy as np
import pandas as pd

# Define the differential equation y' = e^(t - y)
def f(t, y):
    return np.exp(t - y)

# Exact solution for comparison
def y_exact(t):
    return np.log(np.exp(t) + np.exp(-1))

# Initial condition
y0 = 1
t0 = 0
t_end = 1.0

# Step sizes
h_euler = 0.05  # Euler method step size
h_midpoint = 0.1  # Midpoint method step size
h_rk4 = 0.2  # RK4 method step size

# Generate time points
t_values_euler = np.arange(t0, t_end + h_euler, h_euler)
t_values_midpoint = np.arange(t0, t_end + h_midpoint, h_midpoint)
t_values_rk4 = np.arange(t0, t_end + h_rk4, h_rk4)

# Euler Method
y_euler = [y0]
for t in t_values_euler[:-1]:
    y_euler.append(y_euler[-1] + h_euler * f(t, y_euler[-1]))
y_euler = np.array(y_euler)
errors_euler = np.abs(y_exact(t_values_euler) - y_euler)

# Midpoint Method
y_midpoint = [y0]
for t in t_values_midpoint[:-1]:
    y_temp = y_midpoint[-1] + (h_midpoint / 2) * f(t, y_midpoint[-1])
    y_midpoint.append(y_midpoint[-1] + h_midpoint * f(t + h_midpoint / 2, y_temp))
y_midpoint = np.array(y_midpoint)
errors_midpoint = np.abs(y_exact(t_values_midpoint) - y_midpoint)

# RK4 Method
y_rk4 = [y0]
for t in t_values_rk4[:-1]:
    k1 = h_rk4 * f(t, y_rk4[-1])
    k2 = h_rk4 * f(t + h_rk4 / 2, y_rk4[-1] + k1 / 2)
    k3 = h_rk4 * f(t + h_rk4 / 2, y_rk4[-1] + k2 / 2)
    k4 = h_rk4 * f(t + h_rk4, y_rk4[-1] + k3)
    y_rk4.append(y_rk4[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
y_rk4 = np.array(y_rk4)
errors_rk4 = np.abs(y_exact(t_values_rk4) - y_rk4)

# Create error tables
error_table_euler = pd.DataFrame({'t': t_values_euler, 'error_euler': errors_euler})
error_table_midpoint = pd.DataFrame({'t': t_values_midpoint, 'error_midpoint': errors_midpoint})
error_table_rk4 = pd.DataFrame({'t': t_values_rk4, 'error_rk4': errors_rk4})

# Create data tables
df_euler = pd.DataFrame({'t': t_values_euler, 'y_euler': y_euler, 'error_euler': errors_euler})
df_midpoint = pd.DataFrame({'t': t_values_midpoint, 'y_midpoint': y_midpoint, 'error_midpoint': errors_midpoint})
df_rk4 = pd.DataFrame({'t': t_values_rk4, 'y_rk4': y_rk4, 'error_rk4': errors_rk4})

# Display tables
print("Euler Method Results:")
print(df_euler)
print("\nMidpoint Method Results:")
print(df_midpoint)
print("\nRK4 Method Results:")
print(df_rk4)

print("--------------------------")

# Display error tables
print("Euler Method Error Table:")
print(error_table_euler)
print("\nMidpoint Method Error Table:")
print(error_table_midpoint)
print("\nRK4 Method Error Table:")
print(error_table_rk4)
