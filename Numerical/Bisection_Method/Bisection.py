import math

# Function 
def f(x):
    return math.log(x) - 1

# Bisection method
def bisection(a, b, tol):
    n = 0
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print("Function values at the endpoints must be of opposite signs.")
        return None
    
    print("n | a_n      | b_n      | p_n      | f(p_n)")
    print("-" * 47)
    
    while (b - a) / 2 > tol:
        p = (a + b) / 2
        fp = f(p)
        print(f"{n} | {a:.6f} | {b:.6f} | {p:.6f} | {fp:.6f}")
        
        if fp == 0:  # Found exact root
            break
        
        if fa * fp < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp
        
        n += 1

    # Final result
    p = (a + b) / 2
    fp = f(p)
    print(f"{n} | {a:.6f} | {b:.6f} | {p:.6f} | {fp:.6f}")
    
    print(f"\nNumber of iterations: {n}")
    return p

# Initial interval and tolerance
a = 2
b = 3
tol = 1e-3

# Compute the root
root = bisection(a, b, tol)
print(f"Root found: {root:.6f}")


