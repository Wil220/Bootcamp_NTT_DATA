while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    if opcao == 1:
        print("Sacabdo...")
    elif opcao == 2:
        print("Exibindo extrato...")
    elif opcao == 0:
        print("Saindo...")
else:
    print("Opção não encontrada ")
