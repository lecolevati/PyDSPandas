import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=';')
# print(dados.head(30))
# print(dados.head(30).to_string())

#Distribuição de frequência
# Quantidade de imóveis com 1 ou 2 quartos
# Quantidade de imóveis com 3 ou 4 quartos
# Quantidade de imóveis com 5 ou 6 quartos
# Quantidade de imóveis com mais de 7 quartos
classes = [0, 2, 4, 6, 100]
quartos = pd.cut(dados['Quartos'], classes)
# print(quartos)
grupos_por_quartos = pd.value_counts(quartos)
# print(grupos_por_quartos)

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']
quartos = pd.cut(dados['Quartos'], classes, labels = labels)
# print(quartos)
grupos_por_quartos_com_labels = pd.value_counts(quartos)
# print(grupos_por_quartos_com_labels)

quartos = pd.cut(dados['Quartos'], classes, labels = labels, include_lowest=True)
# print(quartos)
grupos_por_quartos_com_labels = pd.value_counts(quartos)
print(grupos_por_quartos_com_labels)