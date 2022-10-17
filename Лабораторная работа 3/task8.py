money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
while money_capital >= spend: # пока капитал может покрыть следующий расход
    money_capital = money_capital + salary - spend # добавка к подушке б. (после первого месяца - к капиталу) з/п минус расход
    spend = spend * (1 + increase)
    month = month + 1
# TODO Оформить решение

print(month)
