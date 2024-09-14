opcao = int(input("Digite a opção desejada: [1] sacar \n [2] extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato... ")
else: 
    print("Opção invalida ")