import pandas as pd

dados = pd.read_csv("aluguel_residencial.csv", sep=';')
# print(dados.head(30))

dados['Valor Total'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
# print(dados.head(30).to_string())

dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)
# print(dados.head(30).to_string())

dados['Valor Total m2'] = (dados['Valor Total'] / dados['Area']).round(2)
# print(dados.head(30).to_string())

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
# print(dados.head(30).to_string())

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Total', 'Valor Total m2']])
# print(dados_aux.head(30).to_string())
del dados_aux['Valor Total']
# print(dados_aux.head(30).to_string())
dados_aux.pop('Valor Total m2')
# print(dados_aux.head(30).to_string())
dados.drop(['Valor Total', 'Valor Total m2'], axis=1, inplace=True)
# print(dados.head(30).to_string())

dados.to_csv("aluguel_residencial.csv", sep=';', index=False)
