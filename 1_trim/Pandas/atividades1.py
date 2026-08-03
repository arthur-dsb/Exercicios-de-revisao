import pandas as pd
#Q1

df = pd.read_csv('jogos.csv')
print(f'''==========DATAFRAME==========
{df}
=============================''')
'''
#a)
linhas,colunas = df.shape
print(f'Há {linhas} jogos no dataset')
#b)
print(df.info())
#c)
print(df[['nota', 'preco']].mean())
#d)
print(df[['jogo','preco']].head(3))
'''
#Q2
print(df['genero'].value_counts())           # Minha previsão: contagem dos valores
print(df['nota'].max())                       # Minha previsão: valor máximo
print(df['preco'].min())                      # Minha previsão: valor mínimo
print(df.loc[5, 'jogo'])                      # Minha previsão: exibe jogo na linha 5
print(df.iloc[0:3, 1:3])                      # Minha previsão: exibe o item das colunas 0 a 3 e das linhas 1 a 3
print(df[['jogo', 'ano']].tail(3))            # Minha previsão: exibe os últimos 3 itens das colunas jogo e ano
print(df.describe().loc['mean'])             # Minha previsão: descreve se o dataset é inteiro ou decimal
