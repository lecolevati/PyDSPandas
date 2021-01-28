import pandas as pd

data = [1, 2, 3, 4, 5]
# s = pd.Series(data)
# print(s)

index = ['Linha ' + str(i) for i in range(0, 5)]
# print(index)

s = pd.Series(data=data, index=index)
# print(s)

data = {'Linha ' + str(i) : i + 1 for i in range(0, 5)}
# print(data)
s = pd.Series(data)
# print(s)

s1 = s + 2
# print(s1)

s2 = s + s1
# print(s2)

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
df1 = pd.DataFrame(data=data)
# print(df1)
index = ['Linha ' + str(i) for i in range(3)]
# print(index)
df1 = pd.DataFrame(data=data, index=index)
# print(df1)
columns = ['Coluna ' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index, columns=columns)
# print(df1)

data = {'Coluna 0': {'Linha 0': 1, 'Linha 1': 4, 'Linha 2': 7},
        'Coluna 1': {'Linha 0': 2, 'Linha 1': 5, 'Linha 2': 8},
        'Coluna 2': {'Linha 0': 3, 'Linha 1': 6, 'Linha 2': 9}}
df2 = pd.DataFrame(data)
# print(df2)

data = [(1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)]
df3 = pd.DataFrame(data=data, index=index, columns=columns)
# print(df3)


df1[df1 > 0] = 'A'
df2[df2 > 0] = 'B'
df3[df3 > 0] = 'C'
# print(df1)
# print(df2)
# print(df3)

df4 = pd.concat([df1, df2, df3])
# print(df4)

df4 = pd.concat([df1, df2, df3], axis=1)
# print(df4)


df1 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df2 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
print(pd.concat([df1, df2]))

dados = [('A', 'B'), ('C', 'D')]
df = pd.DataFrame(dados, columns = ['L1', 'L2'],  index = ['C1', 'C2'])
print(df)

dados = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(dados, index, columns)
print(df)

dados = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(dados)
print(df)
