def newton_raphson_sqrt(k, epsilon=0.01):
    guess = k / 2
    while abs(guess**2 - k) >= epsilon:
        guess = guess - ((guess**2 - k) / (2 * guess))
    return guess
k = 12345
result = newton_raphson_sqrt(k)
print('Square root of', k, 'is about', result)