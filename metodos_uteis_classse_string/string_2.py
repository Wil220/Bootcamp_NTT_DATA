#Old style %
nome = "Wilker"
idade = 25
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome":  "Wilker", "idade":  25, }

print("nome: %s, idade: %d, profissão: %s, linguagem: %s"%(nome, idade, profissao, linguagem ))

print("nome: {}, idade: {}, profissão: {}, linguagem: {}".format(nome, idade, profissao, linguagem ))

print("nome: {3}, idade: {1}, profissão: {2}, linguagem: {0}".format(linguagem, idade, profissao, nome ))
#vantagem codigoa baixo, posso utilizar a variavel mais de uma vez
print("nome: {3}, idade: {1}, profissão: {2}, linguagem: {0}, nome: {3}".format(linguagem, idade, profissao, nome ))

#temos essa outra forma também
print("nome: {nome}, idade: {idade}, profissão: {profissao}, linguagem: {linguagem}, nome: {nome}".format(linguagem=linguagem, idade=idade, profissao=profissao, nome=nome))
print("nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")

