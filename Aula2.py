import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=';')
# print(dados.head(10))
# print(dados.Tipo)
# print(dados['Tipo'])
tipos_de_imovel = dados['Tipo']
# print(type(tipos_de_imovel))
# print(tipos_de_imovel.drop_duplicates())
ti = tipos_de_imovel.drop_duplicates()
# print(ti)

ti = pd.DataFrame(ti)
# print(ti)
# print(ti.index)
# print(ti.shape[0])
# print(range(ti.shape[0]))

# for i in range(ti.shape[0]):
#     print(i)

ti.index = range(ti.shape[0])
ti.columns.name = 'ID'
print(ti)
