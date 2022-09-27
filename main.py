
# 1 КАЛЬКУЛЯТОР))

a = int(input('Введите первое число:'))

b = input('Введите знак:')

c = int(input('Введите второе число:'))

answer = None
if b == '/' and c == 0:
    answer = ' На ноль делить нельзя '

elif b == '+':
    answer = a + c

elif b == '-':
    answer = a - c

elif b == '/':
    answer = a / c

elif b == '*':
    answer = a * c

elif b == '**':
    answer = a ** c

print('Ваш ответ:', answer)

print('-----------------------------------------------------------------')

# Решение 2 задачи!!))

print('Дорогой пользователь, введите начальное и конечное число:')
first_num = int(input('Начальное:'))
second_num = int(input('Конечное:'))

for i in range(first_num, second_num):
    if i**2 <= second_num:
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

