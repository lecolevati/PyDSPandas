import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=';')
# print(dados)
# print(type(dados))
# print(dados.info())
# print(dados.head(10).to_string())
# print(dados.dtypes)

tipos_de_dados = pd.DataFrame(dados.dtypes, columns=["Tipos de Dados"])
tipos_de_dados.columns.name = 'Variaveis'
# print(tipos_de_dados)

# print(dados.shape)
# print(dados.shape[0])
# print(dados.shape[1])

print("A base de dados apresenta {} registros (imóveis) e {} variáveis".format(dados.shape[0], dados.shape[1]))
