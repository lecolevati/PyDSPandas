import pandas as pd

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
# print(df)
#Filtrando colunas
# print(df['c1'])
# print(df[['c3','c1']])

#Filtrando linhas
# print(df[1:]) #Excluindo a 0
# print(df[1:3])  #Apenas de linhas 1 a 3
# print(df[1:][['c3','c1']]) #Excluindo a linha 0 e com as colunas delimitadas

# print(df.loc['l3']) #linha 3 pelo nome
# print(df.loc[['l3','l2']]) #linhas 3 e 2 pelo nome
# print(df.loc['l1','c2']) #localização matricial (linha x coluna) por nome
# print(df.iloc[0, 1]) #localização matricial (linha x coluna) por índice

# print(df.loc[['l3','l1'],['c4', 'c1']]) #mini dataframe com linhas e colunas específicas por nome
# print(df.iloc[[2, 0],[3, 0]]) #mini dataframe com linhas e colunas específicas por índice
