import pandas as pd

# json = open("dados/aluguel.json")
# print(json.read())

# txt = open("dados/aluguel.txt")
# print(txt.read())

# df_json = pd.read_json(("dados/aluguel.json"))
# print(df_json)

# df_txt = pd.read_table(("dados/aluguel.txt"))
# print(df_txt)

# df_xlsx = pd.read_excel(("dados/aluguel.xlsx"))
# print(df_xlsx)

# df_html = pd.read_html(("dados/dados_html_1.html")) #Poderia ser a URL
# print(df_html)

df_html = pd.read_html(("dados/dados_html_2.html"))
# print(len(df_html))
# print(df_html[0])
# print(df_html[1])
# print(df_html[2])
