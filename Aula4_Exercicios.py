import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35],
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
                        'Aprovado': [True, False, False, True, True, True, False, False]},
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])
# print(alunos)

#Alunos (independente de sexo) aprovados
selecao = alunos['Aprovado'] == True
aprovados = alunos[selecao]
# print(aprovados)

#Alunos (independente de sexo) aprovados
selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
aprovadas = alunos[selecao]
# print(aprovadas)

#Alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos
selecao = (alunos.Idade > 10) & (alunos.Idade < 20) | (alunos.Idade >= 40)
idade = alunos[selecao]
# print(idade)

#Alunos reprovados e mantenha neste DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem
selecao = alunos['Aprovado'] == False
reprovados = alunos[selecao]
reprovados = reprovados[['Nome', 'Sexo', 'Idade']]
# print(reprovados)

#Os três alunos mais novos
selecao = alunos.sort_values(by=['Idade'])
idade = selecao.iloc[:3]
print(idade)
