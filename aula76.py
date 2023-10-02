pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Raeder',
    'idade': 11,
    'altura': 1.45,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ],
}

for key in pessoa:
    print(f'{key}: {pessoa[key]}')
