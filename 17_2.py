import random


def Digit(K, N):
    K_str = str(K)
    if len(K_str) < N:
        return -1
    return int(K_str[-N])

K1 = random.randint(1, 10000)
K2 = random.randint(1, 100000)
K3 = random.randint(1, 1000000)
K4 = random.randint(1, 10000000)
K5 = random.randint(1, 100000000)
for N in range(1, 6):
    digit_K1 = Digit(K1, N)
    digit_K2 = Digit(K2, N)
    digit_K3 = Digit(K3, N)
    digit_K4 = Digit(K4, N)
    digit_K5 = Digit(K5, N)

    print(f"N = {N}:")
    print(f"K1: {K1}, {N}-я цифра: {digit_K1}")
    print(f"K2: {K2}, {N}-я цифра: {digit_K2}")
    print(f"K3: {K3}, {N}-я цифра: {digit_K3}")
    print(f"K4: {K4}, {N}-я цифра: {digit_K4}")
    print(f"K5: {K5}, {N}-я цифра: {digit_K5}")
    print()
