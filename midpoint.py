import matplotlib.pyplot as plt

def midpoint(f, a, ya, b, n):
    i = 0
    x = [a]
    y = [ya]
    h = (b - a) / n
    
    while i < n:
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h/2 * k1)
        y_next = y[i] + h * k2
        x_next = a + (b - a) * (i + 1) / n

        y.append(y_next)
        x.append(x_next)
        i += 1

    return y, x

def f(x, y):
    return x * y  

a = 0.0
ya = 1.0
b = 1.0
n = 100

y, x = midpoint(f, a, ya, b, n)

plt.plot(x, y, label='Midpoint Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation of y(x) using Midpoint Method')
plt.legend()
plt.grid(True)
plt.show()
