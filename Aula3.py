import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=';')
tipos_de_imovel = dados['Tipo']
# print(list(tipos_de_imovel.drop_duplicates()))

residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
# print(residencial)

# print(dados['Tipo'].isin(residencial).head(10))
selecao = dados['Tipo'].isin(residencial)
# print(selecao)

dados_residencial = dados[selecao]
# print(dados_residencial.head(20))

# print(list(dados_residencial['Tipo'].drop_duplicates()))
# print(dados_residencial.shape[0], dados.shape[0])

dados_residencial.index = range(dados_residencial.shape[0])
# print(dados_residencial)

dados_residencial.to_csv('aluguel_residencial.csv', sep=';', index=False)

dados_res_2 = pd.read_csv("aluguel_residencial.csv", sep=';')
print(dados_res_2.head(30))
