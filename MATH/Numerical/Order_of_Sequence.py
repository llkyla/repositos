import numpy as np
import pandas as pd

# Define the exact value of sqrt(5)
exact_value = np.sqrt(5)

# Initialize sequence 1
p1_values = [1.0]  # p_0 = 1.0
n_steps = 10
errors_1 = []

# Function for the recurrence relation of sequence 1
def seq1_next(p_n, n):
    if n == 0:
        return 2 * p_n + p_n / np.sqrt(1)
    return 2 * p_n + p_n / np.sqrt(n)

# Compute the sequence and errors for sequence 1
for n in range(1, n_steps):
    next_value = seq1_next(p1_values[-1], n)
    p1_values.append(next_value)
    errors_1.append(abs(next_value - exact_value))

# Compute ratios
ratios_1 = {
    'en/en-1': [errors_1[i] / errors_1[i-1] if i > 0 else None for i in range(len(errors_1))],
    'en/en-2': [errors_1[i] / errors_1[i-2] if i > 1 else None for i in range(len(errors_1))],
    'en/en-3': [errors_1[i] / errors_1[i-3] if i > 2 else None for i in range(len(errors_1))],
    'en/en-4': [errors_1[i] / errors_1[i-4] if i > 3 else None for i in range(len(errors_1))],
    'en/en-5': [errors_1[i] / errors_1[i-5] if i > 4 else None for i in range(len(errors_1))],
    'en/en-6': [errors_1[i] / errors_1[i-6] if i > 5 else None for i in range(len(errors_1))],
    'en/en-7': [errors_1[i] / errors_1[i-7] if i > 6 else None for i in range(len(errors_1))]

}

# Create dataframe for sequence 1
df_seq1 = pd.DataFrame({
    'n': list(range(1, n_steps)),
    'pn': p1_values[1:],
    'en': errors_1,
    'en/en-1': ratios_1['en/en-1'],
    'en/en-2': ratios_1['en/en-2'],
    'en/en-3': ratios_1['en/en-3'],
    'en/en-4': ratios_1['en/en-4'],
    'en/en-5': ratios_1['en/en-5'],
    'en/en-6': ratios_1['en/en-6'],
    'en/en-7': ratios_1['en/en-7']
}).round(8)

# Display table for sequence 1
print(df_seq1)

##########################

# Define the exact value of sqrt(5)
exact_value = np.sqrt(5)

# Initialize sequence 2
p2_values = [1.0]  # p_0 = 1.0
n_steps = 10
errors_2 = []

# Function for the recurrence relation of sequence 2
def seq2_next(p_n):
    return (p_n**3 + 5 * 3 * p_n) / (3 * p_n**2 + 5)

# Compute the sequence and errors for sequence 2
for n in range(1, n_steps):
    next_value = seq2_next(p2_values[-1])
    p2_values.append(next_value)
    errors_2.append(abs(next_value - exact_value))

# Function to safely divide and handle zero errors
def safe_divide(a, b):
    return a / b if b != 0 else np.nan

# Compute ratios for sequence 2, avoiding division by zero
ratios_2 = {
    'en/en-1': [safe_divide(errors_2[i], errors_2[i-1]) if i > 0 else None for i in range(len(errors_2))],
    'en/en-2': [safe_divide(errors_2[i], errors_2[i-2]) if i > 1 else None for i in range(len(errors_2))],
    'en/en-3': [safe_divide(errors_2[i], errors_2[i-3]) if i > 2 else None for i in range(len(errors_2))],
    'en/en-4': [safe_divide(errors_2[i], errors_2[i-4]) if i > 3 else None for i in range(len(errors_2))],
    'en/en-5': [safe_divide(errors_2[i], errors_2[i-5]) if i > 4 else None for i in range(len(errors_2))],
    'en/en-6': [safe_divide(errors_2[i], errors_2[i-6]) if i > 5 else None for i in range(len(errors_2))]
}

# Create dataframe for sequence 2
df_seq2 = pd.DataFrame({
    'n': list(range(1, n_steps)),
    'pn': p2_values[1:],
    'en': errors_2,
    'en/en-1': ratios_2['en/en-1'],
    'en/en-2': ratios_2['en/en-2'],
    'en/en-3': ratios_2['en/en-3'],
    'en/en-4': ratios_2['en/en-4'],
    'en/en-5': ratios_2['en/en-5'],
    'en/en-6': ratios_2['en/en-6'],
}).round(8)

# Display table for sequence 2
print(df_seq2)
