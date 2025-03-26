def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
