color_one = str(input())
color_two = str(input())
red = 'красный'
blue = 'синий'
yellow = 'желтый'
if color_one == red and color_two == red:
    print(red)
elif color_one == blue and color_two == blue:
    print(blue)
elif color_one == yellow and color_two == yellow:
    print(yellow)
elif color_one == red and color_two == blue or color_two == red and color_one == blue:
    print('фиолетовый')
elif color_one == red and color_two == yellow or color_one == yellow and color_two == red:
    print('оранжевый')
elif color_one == blue and color_two == yellow or color_one == yellow and color_two == blue:
    print('зеленый')
else:
    print('ошибка цвета')