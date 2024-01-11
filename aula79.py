import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1.copy() Cópia rasa, copia os valores imutáveis e linka os imutáveis
d2 = copy.deepcopy(d1)  # Cópia profunda, copia todos os valores

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)
