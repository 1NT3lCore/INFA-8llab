N = int(input("Введите натуральное число: "))

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

result = sum_digits(N)
print("Сумма цифр числа", N, "равна", result)
