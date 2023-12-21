def triangle_area(x, y):
    area = abs((x[0]*(y[1]-y[2]) + x[1]*(y[2]-y[0]) + x[2]*(y[0]-y[1]))/2)
    return area

def compare_areas(xa, ya, xb, yb):
        if len(xa) != 3 or len(ya) != 3 or len(xb) != 3 or len(yb) != 3:
            print("Координаты треугольников должны состоять из трех точек")
            exit()
        area_a = triangle_area(xa, ya)
        area_b = triangle_area(xb, yb)
        if area_a > area_b:
            return 1
        elif area_b > area_a:
            return 2
        else:
            return None

try:
    xa = list(map(float, input("Введите координаты вершин треугольника А по оси OX через пробел: ").split()))
except:
    print("Неверный тип данных")
    exit()
try:
    ya = list(map(float, input("Введите координаты вершин треугольника А по оси OY через пробел: ").split()))
except:
    print("Неверный тип данных")
    exit()
try:
    xb = list(map(float, input("Введите координаты вершин треугольника B по оси OX через пробел: ").split()))
except:
    print("Неверный тип данных")
    exit()
try:
    yb = list(map(float, input("Введите координаты вершин треугольника B по оси OY через пробел: ").split()))
except:
    print("Неверный тип данных")
    exit()

result = compare_areas(xa, ya, xb, yb)
if result == 1:
    print("1")
elif result == 2:
    print("2")
else:
    print("Площади треугольников равны")

