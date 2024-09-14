MAIOR_IDADE = 18
IDADE_ESPECIAL = 1

idade = int(input("Informe sua idade: "))
#Primeira forma de fazer
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH ")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. ")


#Segunda forma
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH ")
else:
    print("Ainda não pode tirar a CMH. ")


#Terceira froma
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH ")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas téoricas mas não pode fazer as aulas praticas! ")
else:
    print("Ainda não pode tirar a CMH. ")

    #ANALOGIA
#Se você tem a idade necessária, você entra na boate e dança (pode tirar a CNH).
#Se você tem uma idade especial, você entra, mas só pode assistir (pode fazer aulas teóricas).
#Se você for muito jovem, você nem entra (não pode tirar a CNH).