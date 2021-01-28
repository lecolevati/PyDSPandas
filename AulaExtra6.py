import pandas as pd

s = pd.Series(list('asdadeadesdasesda'))
# print(s)
print(s.unique())
print(s.value_counts())

dados = pd.read_csv("aluguel.csv", sep=';')
print(dados.Tipo.unique())
print(dados.Tipo.value_counts())
