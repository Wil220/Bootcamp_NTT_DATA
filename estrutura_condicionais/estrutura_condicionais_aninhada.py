CONTA_NORMAL = False
CONTA_UNIVERSITARIA = True

SALDO = 2000
SAQUE = 2500
CHEQUE_ESPECIAL = 450

if CONTA_NORMAL:
    if SALDO >= SAQUE:
        print("Saque realizado com sucesso! ")
    elif  SAQUE <= (SALDO + CHEQUE_ESPECIAL):
        print("Saque realiazado com sucesso com o uso do cheque especial! ")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif CONTA_UNIVERSITARIA:
    if SALDO >= SAQUE:
        print("Saque realizado com sucesso! ")
    else:
        print("Saldo insuficiente")

