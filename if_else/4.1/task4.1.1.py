# При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности,
# поскольку такой подход уменьшает возможность неверного ввода пароля.
#
# Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
#
# Формат входных данных
# На вход программе подаются две строки.
#
# Формат выходных данных
# Программа должна вывести одну строку в соответствии с условием задачи.
# Sample Input 1:
#
# qwerty
# qwerty
# Sample Output 1:
#
# Пароль принят

password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')
    print('some test')
    print('somet additional test')
    print("test")