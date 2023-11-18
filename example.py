def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise TypeError("dividir() deve receber apenas argumentos inteiros")
    try:
        aux = dividendo / divisor
        return aux
    except Exception:
        print(f"Não foi possivel dividir {dividendo} por {divisor}")
        raise


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


testa_divisao(0)

# try:
#     testa_divisao(0)
# except ZeroDivisionError as e:
#     print("Erro de divisao por zero")
# except Exception as e:
#     print("Tratamento generico")

# try:
#     testa_divisao(0)
# except AttributeError as e:
#     print(e.__class__.__bases__)
# except ZeroDivisionError as e:
#     print(e.__class__.__bases__)

# try:
#     print("O fluxo está aqui")
#     raise ValueError
# except Exception:
#     print("Agora ele foi para cá")
#
# print("E enfim ele continua...")
