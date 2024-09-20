#a = int(input("Informe um numero: "))
#print(a)

#a +=1
#print(a)

#a +=1
#print(a)

# essa aplicação procura por alguma letra exemplo, se eu escrever python nas minhas vogais tem o O então eleaparece natela a letra O 
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #Adiciona uma quebra delinha 

#Taubuada

for numero in range(0, 51, 5):
    print(numero) 
