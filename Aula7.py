import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import tkinter
import matplotlib
matplotlib.use( 'tkagg' )


dados = pd.read_csv("aluguel_residencial.csv", sep=';')
# print(dados.head(30))
# print(dados.head(30).to_string())

# print(dados['Valor'].mean())

#Filtro bairro
bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]

# print(dados)
# print(dados['Bairro'].drop_duplicates())

grupo_bairro = dados.groupby('Bairro')
# print(type(grupo_bairro))

# print(grupo_bairro.groups)

# for bairro, dados_bairro in grupo_bairro:
#     print(bairro)
#
# for bairro, dados_bairro in grupo_bairro:
#     print(dados_bairro.to_string())

# for bairro, dados_bairro in grupo_bairro:
#     print('{} -> {}'.format(bairro, dados_bairro.Valor.mean()))

media_valor_condo = grupo_bairro[['Valor', 'Condominio']].mean().round(2)
# print(media_valor_condo)

# print(grupo_bairro['Valor'].describe().round(2).to_string())
# print(grupo_bairro['Valor'].aggregate(['min','max','sum']).to_string())
# print(grupo_bairro['Valor'].aggregate(['min','max']).rename(columns = {'min': 'Minimo', 'max': 'Maximo'}).to_string())

plt.rc('figure', figsize = (20,10))
# grupo_bairro['Valor'].std().plot.bar(color = 'blue')
# plt.show()

fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor Médio do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize' : 22})
plt.show()