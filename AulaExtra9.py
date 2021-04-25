import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize = (15,8))

#Mais sobre gráficos
dados = pd.read_csv("aluguelv2.csv", sep=';')
base = dados.head(30).to_string()
print(base)

#Criando gráfico na figura
area = plt.figure()
g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor x Área')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100) #100 valores aleatórios
# print(dados_g3))
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra Valor')

grupo_g4 = dados.groupby('Tipo')['Valor']
label = grupo_g4.mean().index
valores = grupo_g4.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')

area.savefig('grafico_com_4.png', dpi = 300, bbox_inches = 'tight')


plt.show()