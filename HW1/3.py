n = int(input()) #число поездок
a = n % 60 #колво билетов на 60 
if a >= 36: #просматриваем больше ли 36 поездок по 60 и сокращаем
    t = n // 60 + 1
    n = 0
    m = 0
else:
    t = n // 60 #на 10 поездок и далее по похожей схеме проверяем
    if (a % 10) >= 9:
        n = a // 10 + 1
        m = 0
    else: #также рассматриваем иные случаи
        n = a // 10
        m = a % 10
print(m, n ,t) #радуемся что вроде работает