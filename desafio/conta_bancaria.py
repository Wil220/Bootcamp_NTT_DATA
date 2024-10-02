opcao = int(input("""Digite a opção desejada: 
                  [1] sacar 
                  [2] extrato 
                  [3] depositar
                  """))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato... ")
    
elif opcao == 3:
    print("Depositar")
else: 
    print("Opção invalida ")