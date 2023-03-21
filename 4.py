# 1.4[8]. Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть 
# разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no



chocolate_slices_1 = 3 
chocolate_slices_2 = 2
break_slices = 4
total_slices = chocolate_slices_1 * chocolate_slices_2
if total_slices > break_slices and ((break_slices % chocolate_slices_1 == 0) or
(break_slices % chocolate_slices_2 == 0)):
    print('Yes')
else:
    print('No')
