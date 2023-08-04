def merson(f, a, ya, b, h, eps, N):
    i = 0
    t = [a]
    y = [ya]
    done = False
    evals = 0

    while not done and i < N:
        if (b - t[i] - h) * (b - a) <= 0:
            h = b - t[i]
            done = True

        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/3, y[i] + h/3 * k1)
        k3 = f(t[i] + h/3, y[i] + h/6 * (k1 + k2))
        k4 = f(t[i] + h/2, y[i] + h/8 * (k1 + 3 * k3))
        k5 = f(t[i] + h, y[i] + h/2 * (k1 - 3 * k3 + 4 * k4))
        err = abs(h/30 * (2 * k1 - 9 * k3 + 8 * k4 - k5))
        evals += 5

        if done or err <= eps:
            y_next = y[i] + h/6 * (k1 + 4 * k4 + k5)
            t_next = t[i] + h
            if t_next == t[i]:
                print("Procedure failed. Step size reached zero.")
                return
            y.append(y_next)
            t.append(t_next)
            i += 1

        q = 0.9 * (eps/err)**(1/4)
        q = max(q, 0.1)
        q = min(5.0, q)
        h *= q

    if not done:
        print("Procedure failed. Maximum number of iterations reached.")
    
    return y, t, evals

# Example usage:
def f(x, y):
    return x * y  # Define your function f(x, y) here

a = 0.0
ya = 1.0
b = 1.0
h = 0.1
eps = 1e-5
N = 1000

y, t, evals = merson(f, a, ya, b, h, eps, N)
print("Approximation of the solution:")
for i in range(len(t)):
    print(f"({t[i]}, {y[i]})")
print(f"Total function evaluations: {evals}")
