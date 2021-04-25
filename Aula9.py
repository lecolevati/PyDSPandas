import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize = (14,6))

#Removendo Outliers
dados = pd.read_csv("aluguel_residencial.csv", sep=';')

# dados.boxplot(['Valor'])

excessos = dados[dados['Valor'] >= 500000]
# print(excessos.to_string())

valor = dados['Valor']

Q1 = valor.quantile(.25)
# print(Q1)
Q3 = valor.quantile(.75)
# print(Q3)
IIQ = Q3 - Q1
print(IIQ)
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_in = dados[selecao]
# dados_in.boxplot(['Valor'])

# dados.hist(['Valor'])
# dados_in.hist(['Valor'])

# dados.boxplot(['Valor'], by= ['Tipo'])
grupo_tipo = dados.groupby('Tipo')['Valor']

print(grupo_tipo.groups)

Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

# print(Q1, Q3, IIQ, limite_inferior, limite_superior)
# print(limite_inferior['Apartamento'])
# print(limite_superior['Casa'])

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    # print(tipo)
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

# dados_new.boxplot(['Valor'], by=['Tipo'])
plt.show()

dados_new.to_csv('venv/dados/aluguel_residencial_sem_outliers.csv', sep = ';', index = False)
dados_new.to_csv('aluguel_residencial_sem_outliers.csv', sep = ';', index = False)