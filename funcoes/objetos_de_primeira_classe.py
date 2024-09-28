def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f" O resultado operado e {resultado}")

exibir_resultado(10, 10, somar)