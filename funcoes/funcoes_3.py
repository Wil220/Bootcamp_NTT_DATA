def salvar_carros(marca, modelo, ano, placa):
    #salva carro no banco de dados

    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#ARGUMENTO NÃO NOMEADO
salvar_carros("Fiat", "Uno", 1999, "WIL-1999")
#ARGUMENTO NOMEADO
salvar_carros(marca="Fiat", modelo="Uno", ano="1999" , placa="WIL-1999")
#** DICIOONARIO
salvar_carros(**{"marca": "Fiat", "modelo": "Uno", "ano": 1999, "placa": "WIL-1999"})