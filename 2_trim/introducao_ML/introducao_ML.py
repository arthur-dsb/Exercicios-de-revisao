import pandas as pd
#PARTE 1
# 1. Carregar o novo dataset correto
df = pd.read_csv('game_dataset.csv')

# 2. Inspeção geral
print("--- Dimensões do Dataset ---")
l,c = df.shape
print(f"Linhas: {l} | Colunas: {c}\n")

print("--- Tipos de Dados e Valores Ausentes ---")
print(df.info())

print("\n--- Contagem de Duplicatas ---")
print(f"Total de linhas duplicadas: {df.duplicated().sum()}")

# 3. Descarte de colunas irrelevantes
# 'Nome do Jogo' é apenas um identificador textual único que causaria overfitting.
df_limpo = df.drop(columns=['Nome do Jogo'])

# 4. Remoção de linhas duplicadas
df_limpo = df_limpo.drop_duplicates()
print(f"\nNovo tamanho do dataframe após remover duplicatas: {df_limpo.shape}")


#PARTE 2
# 1. Tratamento da 'Classificação de Usuários' (Numérica)
mediana_classificacao = df_limpo['Classificação de Usuários'].median()
df_limpo['Classificação de Usuários'] = df_limpo['Classificação de Usuários'].fillna(mediana_classificacao)

# 2. Tratamento da 'Idade Recomendada' (Numérica/Ordinal discreta)
mediana_idade = df_limpo['Idade Recomendada'].median()
df_limpo['Idade Recomendada'] = df_limpo['Idade Recomendada'].fillna(mediana_idade)

print("Valores ausentes após o tratamento:")
print(df_limpo[['Classificação de Usuários', 'Idade Recomendada']].isna().sum())



#PARTE 3
# 1. Label Encoding (ou mapeamento manual) para a variável binária
# Como 'Lançamento no Brasil' tem apenas duas categorias (Sim/Não), convertemos para 1 e 0.
df_limpo['Lançamento no Brasil'] = df_limpo['Lançamento no Brasil'].map({'Sim': 1, 'Não': 0})

# 2. One-Hot Encoding para as variáveis com mais de duas categorias (Gênero e Plataforma)
df_transformado = pd.get_dummies(df_limpo, columns=['Gênero', 'Plataforma'], drop_first=True)

# Garantir que as colunas booleanas geradas pelo get_dummies virem 0 e 1 numéricos
colunas_bool = df_transformado.select_dtypes(include='bool').columns
df_transformado[colunas_bool] = df_transformado[colunas_bool].astype(int)

print(f"Estrutura dos dados após o Encoding: {df_transformado.shape}")



#PARTE 4
from sklearn.model_selection import train_test_split

# Definindo a variável alvo (y) como o Preço e as demais como features (X)
X = df_transformado.drop(columns=['Preço'])
y = df_transformado['Preço']

# Divisão em 80% para treino e 20% para teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Formato do Treino: {X_treino.shape} | Formato do Teste: {X_teste.shape}")



#PARTE 5
from sklearn.preprocessing import StandardScaler

# Selecionando apenas as colunas puramente numéricas que possuem escalas bem distintas
colunas_continuas = ['Classificação de Usuários', 'Vendas Globais', 'Idade Recomendada']

# Inicializando o Z-Score Normalizer (StandardScaler)
scaler = StandardScaler()

# Ajustando (fit) e transformando o treino
X_treino_scaled = X_treino.copy()
X_treino_scaled[colunas_continuas] = scaler.fit_transform(X_treino[colunas_continuas])

# Apenas aplicando (transform) no conjunto de teste
X_teste_scaled = X_teste.copy()
X_teste_scaled[colunas_continuas] = scaler.transform(X_teste[colunas_continuas])

print("Visualização das colunas numéricas normalizadas no Treino:")
print(X_treino_scaled[colunas_continuas].head())



#DESAFIO!
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Instanciar o algoritmo de regressão
modelo_jogo = RandomForestRegressor(n_estimators=100, random_state=42)

# 2. Treinar o modelo com os dados perfeitamente preparados e escalados
modelo_jogo.fit(X_treino_scaled, y_treino)

# 3. Realizar as previsões usando o conjunto de teste isolado
previsoes_preco = modelo_jogo.predict(X_teste_scaled)

# 4. Avaliação de Desempenho usando MAE e R²
mae = mean_absolute_error(y_teste, previsoes_preco)
r2 = r2_score(y_teste, previsoes_preco)

print("\n--- Relatório de Desempenho do Modelo ---")
print(f"Erro Médio Absoluto (MAE): R$ {mae:.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")











