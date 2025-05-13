import pandas as pd
import os

caminho_arquivo_compilado = r'/mnt/hd/Projetos/dadosfut/times_compilados.csv'

df_compilado = pd.read_csv(caminho_arquivo_compilado)

remover = ['sport_id', 'gender', 'founded', 'type', 'placeholder', 'last_played_at', 'Unnamed: 0']

df_tratado = df_compilado.drop(columns=remover)

print(df_tratado.head)

caminho_final = 'times_compilados_tratados.csv'
df_tratado.to_csv(caminho_final, index=False)