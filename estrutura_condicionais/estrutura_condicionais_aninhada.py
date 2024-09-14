CONTA_NORMAL = False
CONTA_UNIVERSITARIA = False
CONTA_ESPECIAL = True

SALDO = 2000
SAQUE = 1500
CHEQUE_ESPECIAL = 450

#Ambos os codigos precisam estar com a infomaçoes desejadas para saque realizado, saque cheque especial ou saldo insuficiente 
#Roda esse bloco caso a conta_normal for True ea conta_universitaria for false 
if CONTA_NORMAL:
    
    if SALDO >= SAQUE:
        print("Saque realizado com sucesso! ")
    elif  SAQUE <= (SALDO + CHEQUE_ESPECIAL):
        print("Saque realiazado com sucesso com o uso do cheque especial! ")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

#Roda essse bloco caso a conta_normal for False ea conta_universitaria for True
elif CONTA_UNIVERSITARIA:

    if SALDO >= SAQUE:
        print("Saque realizado com sucesso! ")
    else:
        print("Saldo insuficiente")

elif CONTA_ESPECIAL:
    print("Conta especial selecionada! ")

#Aparece na telacaso as condiçoes forem falsa falsa
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato cm seu gerente.")