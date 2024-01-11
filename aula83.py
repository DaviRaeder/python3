# Métodos

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
# print(s1)

# Operadores
# União | união (union) - Une
# Intersecção & (intersection) - Itens presentes em ambos
# Diferença - Itens presentes apenas no set da esquerda
# Diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
# print(s3)

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.upper())

    if 'L' in letras:
        print('Parabéns!')
        break

    print(letras)
