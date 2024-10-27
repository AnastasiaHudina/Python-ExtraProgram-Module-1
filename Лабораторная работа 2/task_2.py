import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


total_salary = 0
money_capital = 0
for i in range(1, months+1):
    if i > 1:
        spend = spend + (increase * spend)
    money_capital = money_capital + (spend - salary) # записываем в новую переменную сколько не хватило
#print(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))
