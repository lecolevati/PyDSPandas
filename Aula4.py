import pandas as pd

dados = pd.read_csv("aluguel_residencial.csv", sep=';')
# print(dados.head(10).to_string())

# Apenas imóveis Apartamento
selecao = dados['Tipo'] == 'Apartamento'
# print(selecao)
n1 = dados[selecao].shape[0]
# print(n1)

#Apenas imóveis Casa, Casa de Condomínio ou Casa de Vila
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
# print(n2)

#Apenas imóveis que tenham entre 60 e 100 m²
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
# print(n3)

#Apenas os que tem pelo menos 4 quartos e Aluguel inferior a R$2000.00
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000.0)
n4 = dados[selecao].shape[0]
# print(n4)

print("Nº de imóveis Apartamento -> {}".format(n1))
print("Nº de imóveis Casa, Casa de Condomínio ou Casa de Vila -> {}".format(n2))
print("Nº de imóveis que tenham entre 60 e 100 m² -> {}".format(n3))
print("Nº de imóveis que tem pelo menos 4 quartos e Aluguel inferior a R$2000.00 -> {}".format(n4))

