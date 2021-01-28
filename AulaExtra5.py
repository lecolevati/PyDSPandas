import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
# print(s)

#inplace torna a alteração válida no dataframe
# s.fillna(0, inplace=True)
# s.fillna(method='ffill', inplace=True) #Preenche nulos com o valor anterior válido
# s.fillna(method='bfill', inplace=True) #Preenche nulos com o valor posterior válido
# s.fillna(s.mean(), inplace=True) #Preenche nulos com a média entre valores válidos

# s.fillna(method='ffill', limit=1, inplace=True) #Preenche nulos com o valor anterior válido limitado a 1 preenchimento
# s.fillna(method='bfill', limit=1, inplace=True) #Preenche nulos com o valor anterior válido limitado a 1 preenchimento
print(s)
