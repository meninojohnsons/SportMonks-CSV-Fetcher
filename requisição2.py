import pandas as pd
import os

# Substitua 'dados_finais.csv' pelo nome do seu arquivo tratado
caminho_arquivo_final = 'dados_finais.csv'
df_final = pd.read_csv(caminho_arquivo_final)
caminho_arquivo_ids_temporada = 'id_temporada - LIGAS.csv'
df_ids_temporada = pd.read_csv(caminho_arquivo_ids_temporada)

# Exibe as primeiras linhas dos DataFrames para verificação
print("df_final:")
print(df_final.head())
print("\ndf_ids_temporada:")
print(df_ids_temporada.head())

base_url = "https://api.sportmonks.com/v3/football/teams/{id}?filter=teamstatisticSeasons={id_temporada}&include=statistics.details.type&api_token=Np42fowzKoIzywGcvWYk5rs21xcy3VDHAQZRVhXL56xVqjTQj3j47ZBL0NjO"
urls_geradas = []

# Cria um dicionário de mapeamento para facilitar a busca do id_temporada
mapeamento_temporada_id = df_ids_temporada.set_index('temporada')['id_temporada'].to_dict()

# Agrupa os dados por time e temporada para evitar duplicações
grouped = df_final.groupby(['id', 'temporada', 'pais']).first().reset_index()

# Itera sobre cada grupo único de time e temporada para gerar uma URL
for index, row in grouped.iterrows():
    team_id = row['id']
    temporada = row['temporada']
    pais = row['pais']

    # Busca o id_temporada correspondente
    id_temporada = mapeamento_temporada_id.get(temporada)

    if id_temporada:
        url = base_url.format(id=team_id, id_temporada=id_temporada)
        urls_geradas.append({'pais': pais, 'temporada': temporada, 'team_id': team_id, 'url': url})
    else:
        print(f"Aviso: Não foi encontrado id_temporada para a temporada '{temporada}' do time com ID '{team_id}' e país '{pais}'.")

# Exibe as URLs geradas
df_urls = pd.DataFrame(urls_geradas)
print(df_urls)

# Se quiser salvar as URLs em um arquivo CSV
df_urls.to_csv('urls_api_sportmonks_por_time.csv', index=False)