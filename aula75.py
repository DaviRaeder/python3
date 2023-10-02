# Closure

# def multiplicar(numero):
#     def multiplicador(multiplicador):
#         return f'{numero} x {multiplicador} = {numero * multiplicador}'
#     return multiplicador


# duplicar = multiplicar(2)
# triplicar = multiplicar(2)
# quadruplicar = multiplicar(2)

# print(duplicar(2))
# print(triplicar(3))
# print(quadruplicar(4))


def duplicar_triplicar_quadruplicar(num):
    print(num * 2)

    def triplicar():
        print(num * 3)

        def quadruplicar():
            print(num * 4)

        quadruplicar()
    triplicar()


duplicar_triplicar_quadruplicar(4)
