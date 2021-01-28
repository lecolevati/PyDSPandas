import pandas as pd

dados = pd.read_csv("aluguel_residencial.csv", sep=';')
# print(dados.isnull())
# print(dados.notnull())

# print(dados.info())


# print(dados[dados['Valor'].isnull()])

cont_dados = dados.shape[0]
# print(cont_dados)
dados.dropna(subset = ['Valor'], inplace=True)
cont_dados_valor_not_null = dados.shape[0]
# print(cont_dados_valor_not_null)

# print(dados[dados['Condominio'].isnull()].shape[0])


selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
cont_ap_cond_null = dados.shape[0]
dados = dados[~selecao] #Dados removendo apartamentos com condomínio null
cont_ap_cond_not_null = dados.shape[0]
# print (cont_ap_cond_null - cont_ap_cond_not_null)

# print(dados[dados['Condominio'].isnull()].shape[0])

dados = dados.fillna({'Condominio':0, 'IPTU':0})
# print(dados[dados['Condominio'].isnull()].shape[0])
# print(dados[dados['IPTU'].isnull()].shape[0])
# print(dados.head(30))
# print(dados.info())

dados.to_csv("aluguel_residencial.csv", sep=';', index=False)
