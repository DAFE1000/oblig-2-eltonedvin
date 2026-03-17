import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Funksjonen og den deriverte satt lik null
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Finn toppunkt med fsolve (startgjett x=2)
x_max = fsolve(g, 2)[0]
y_max = f(x_max)

print(f"Toppunkt: ({x_max:.4f}, {y_max:.4f})")

# Plot
x = np.linspace(-10, 15, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), color='#2563eb', linewidth=2, label=r'$f(x) = e^{-x/4} \cdot \arctan(x)$')
plt.plot(x_max, y_max, 'ro', markersize=10, label=f'Toppunkt ({x_max:.4f}, {y_max:.4f})')
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$f(x) = e^{-x/4} \cdot \arctan(x)$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
