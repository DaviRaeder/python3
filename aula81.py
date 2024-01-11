perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0

for pergunta in range(len(perguntas)):
    op0 = 2
    op1 = 0
    op2 = 1
    print(perguntas[pergunta]['Pergunta'])
    print('Opções:')
    i = 0
    while i < len(perguntas[pergunta]['Opções']):
        print(f'{i}) {perguntas[pergunta]["Opções"][i]}')
        i += 1
    resposta = input('Escolha uma opção: ')
    if pergunta == 0 and int(resposta) == op0:
        print('Acertou 👍 \n')
        contador += 1
    if pergunta == 1 and int(resposta) == op1:
        print('Acertou 👍 \n')
        contador += 1
    if pergunta == 2 and int(resposta) == op2:
        print('Acertou 👍 \n')
        contador += 1
    if pergunta == 0 and int(resposta) != op0 or pergunta == 1 and int(resposta) != op1 or pergunta == 2 and int(resposta) != op2:
        print('Errou ❌ \n')

print(f'Você acertou {contador} \nde {len(perguntas)} perguntas')
