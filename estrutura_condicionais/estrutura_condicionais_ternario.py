saldo = 2000
saque = 1000

#Tudo que esta no começo sera retornado se a expreção for verdaderia e o que esta no final se a condição for falsa
status = "sucesso" if saldo >= saque else "Falha"

print(f"{status} Ao realizar o saque! ")