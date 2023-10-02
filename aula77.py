pessoa = {}

chave = 'nome'

pessoa[chave] = 'Davi'
pessoa['sobrenome'] = 'Raeder'

print(pessoa[chave])

pessoa[chave] = 'Luiz'

# del pessoa['sobrenome']
print(pessoa)
# print(pessoa['sobrenome']) Key error
print(pessoa['nome'])

# print(pessoa.get('sobrenome', 'Não existe'))
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
