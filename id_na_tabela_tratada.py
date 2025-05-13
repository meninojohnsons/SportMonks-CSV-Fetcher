import pandas as pd
import os

caminho_arquivo_ids_temporada = 'id_temporada - LIGAS.csv'
caminho_df_tratado = 'times_compilados_tratados.csv'
df_ids_temporada = pd.read_csv(caminho_arquivo_ids_temporada)
df_tratado = pd.read_csv(caminho_df_tratado)

# Seleciona apenas as colunas 'temporada' e 'id_temporada'
df_ids_temporada = df_ids_temporada[['temporada', 'id_temporada']]

# Renomeia a coluna 'temporada' para 'periodo_temporada' para evitar confusão
df_ids_temporada = df_ids_temporada.rename(columns={'temporada': 'periodo_temporada'})

# Realiza o merge dos DataFrames
df_final = pd.merge(df_tratado, df_ids_temporada, left_on='temporada', right_on='periodo_temporada', how='left')

# Salva o DataFrame final em um novo arquivo CSV
caminho_arquivo_final = 'dados_finais.csv'
df_final.to_csv(caminho_arquivo_final, index=False)
print(f"\nTabela final salva com sucesso em '{caminho_arquivo_final}'")