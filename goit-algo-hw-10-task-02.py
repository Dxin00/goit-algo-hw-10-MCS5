import numpy as np
import random
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2
N = 1000000

x = np.random.uniform(a, b, N)
y = np.random.uniform(0, f(b), N)

count = np.sum(y < f(x))

S = (b - a) * f(b)

integral_mc = S * count / N

integral_analytical = 8 / 3

integral_quad, _ = spi.quad(f, a, b)

print("Інтеграл (Монте-Карло):", integral_mc)
print("Інтеграл (аналітично):", integral_analytical)
print("Інтеграл (quad):", integral_quad)

print("Абсолютна похибка (Монте-Карло):", abs(integral_mc - integral_analytical))
print("Абсолютна похибка (quad):", abs(integral_quad - integral_analytical))

