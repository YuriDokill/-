def calculate_rectangle_area(width, length):
    area = width * length
    return area
width = 5
length = 10
print(f'Площадь прямоугольника равна -', calculate_rectangle_area(width, length))

#а тут чуть понятнее записано
width1 = 10
length1 = 9
area1 = calculate_rectangle_area(width1, length1)
print(f'Площадь прямоугольника со сторонами {width1} и длиной {length1} равна - {area1}')