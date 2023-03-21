# 1.3[6]. Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет 
# с номером.Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – 
# счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no


number_ticket = 252621
first_three_numbers = number_ticket // 1000
last_three_numbers = number_ticket % 1000
sum_first_three = (first_three_numbers // 100) + (first_three_numbers % 100 // 10) + (first_three_numbers % 10)
sum_last_three = (last_three_numbers // 100) + (last_three_numbers % 100 // 10) + (last_three_numbers % 10)
print(f'Билет {number_ticket} счастливый') if sum_first_three == sum_last_three else print(f'Билет {number_ticket} несчатливый')












# (*) Усложнение. Вывод результат на экран сделайте одной 
# строкой(только один print), для этого используйте 
# тернарный оператор