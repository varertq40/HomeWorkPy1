# 1.1[2]. Найдите сумму цифр трехзначного числа. 
# Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1


number = 123
sum = number // 100
sum1 = number % 100 // 10
sum2 = number % 10
print(f'Сумма числа {number} равна {sum + sum1 + sum2}')
