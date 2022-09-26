
# 1 КАЛЬКУЛЯТОР))

a = int(input('Введите первое число:'))

b = input('Введите знак:')

cal = int(input('Введите второе число:'))

answir = None

if b == '+':
    answir = a + cal

elif b == '-':
    answir = a - cal

elif b == '/':
    answir = a / cal

elif b == '*':
    answir = a * cal

elif b == '**':
    answir = a ** cal

print('Ваш ответ:', answir)

print('-----------------------------------------------------------------')

# Решение 2 задачи!!))

print('Дорогой пользователь, введите начальное и конечное число:')
aa = int(input('Начальное:'))
bb = int(input('Конечное:'))


for i in range(aa, bb):
    if i**2 <= bb:
        print(i**2, end=' ')
print()
print('-----------------------------------------------------------------')

# Простое или Составное?

n = int(input('Введите число:'))

if n == 2 or n == 3 or n == 5 or n == 7:
    print(f'{n} - Простое')
elif n == 1:
    print(f'{n} - Не Простое')

elif n % 2 == 0 or n % 3 ==0 or n % 4 == 0 or n % 5 == 0 or n % 6 == 0 or n % 7 == 0 or n % 8 == 0 or n % 9 == 0:
    print(f'{n} - Составное')
else:
    print(f'{n} - Простое')
