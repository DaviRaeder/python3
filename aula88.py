import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []

for numero in range(1, 11):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(1, 11)
]
# print(list(range(1, 11)))
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
# print(*novos_produtos, sep='\n')

# p(novos_produtos)

# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if 20 <= produto['preco'] > 10
]
p(novos_produtos)
