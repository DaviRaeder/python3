def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


print(multiplica(3, 7, 9))
print(3 * 7 * 9)


def par_impar(num):
    if num % 2 == 0:
        return print(f'O número {num} é par')
    elif num % 2 != 0:
        return print(f'O número {num} é ímpar')
    return print('Digite um valor válido')


par_impar(637262827672852476290651982062980739476207626635918561985617562589652096726256256295629862865206262701967184376810761086786716712906785765967206716106716858161847816716872368)
