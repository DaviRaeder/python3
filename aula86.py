def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         def multiplica2(numero2):
#             return (numero + numero2) * multiplicador
#         return multiplica2
#     return multiplica


duplica = executa(
    lambda m: lambda n: lambda n2: (n + n2) * m,
    2
)
duplica2 = duplica(3)
print(duplica2(2))


print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
