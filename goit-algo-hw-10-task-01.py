import pulp

prob = pulp.LpProblem("Виробництво напоїв", pulp.LpMaximize)

x1 = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

prob += x1 + x2, "Загальна кількість напоїв"

prob += 2*x1 + x2 <= 100, "Обмеження води"
prob += x1 <= 50, "Обмеження цукру"
prob += x1 <= 30, "Обмеження лимонного соку"
prob += 2*x2 <= 40, "Обмеження фруктового пюре"

prob.solve()

print("Статус:", pulp.LpStatus[prob.status])
print("Оптимальне виробництво:")
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Максимальна загальна кількість напоїв =", pulp.value(prob.objective))
