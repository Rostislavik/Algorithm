from collections import namedtuple, deque

QUARTERS = 4
Company = namedtuple('Company', 'name quarters profit')
all_companies = set()

num = int(input("Кол-во компаний: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Название компании {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'прибыль за {j + 1} - й квартал: ')))
        profit += quarters[j]
    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

AVG = total_profit / num

print('\nСредняя прибыль компаний за все кварталы = {AVG}')

print('\nКомпании с прибылью выше средней:')
for comp in all_companies:
    if comp.profit > AVG:
        print(f'Компания {comp.name} заработала {comp.profit}')

print('\nКомпании с прибылью ниже средней:')
for comp in all_companies:
    if comp.profit < AVG:
        print(f'Компания {comp.name} заработала {comp.profit}')
