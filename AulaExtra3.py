import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
linhas = list('321')
colunas = list('zyx')

df = pd.DataFrame(data, linhas, colunas)
# print(df)
print(df.sort_index(axis=1))
print(df.sort_values(by='x'))
