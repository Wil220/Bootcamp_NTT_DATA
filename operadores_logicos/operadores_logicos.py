# AND = para ser True todos tem que ser True
# OR =para ser True apenas um tem que ser True


print(True and True) 
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = False

exp = (saque >= saldo and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)












