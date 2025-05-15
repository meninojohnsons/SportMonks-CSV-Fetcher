import os
import re
import pandas as pd
from .api_handler import ApiHandler

class FileHandler:
    def __init__(self, config):
        self.config = config
        self.api = ApiHandler(config)

    def read_csv(self, path):
        """Lê um CSV em um DataFrame."""
        return pd.read_csv(path)

    def write_csv(self, df, path):
        """Escreve um DataFrame em CSV, criando diretório se necessário."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)

    def get_compiled_path(self):
        return os.path.join(self.config.DATA_FOLDER, 'output', 'times_compilados.csv')

    def get_tratado_path(self):
        return os.path.join(self.config.DATA_FOLDER, 'output', 'times_compilados_tratados.csv')

    def get_final_data_path(self):
        return os.path.join(self.config.DATA_FOLDER, 'output', 'dados_finais.csv')

    def drop_columns(self, df):
        """Remove colunas indesejadas de um DataFrame."""
        remover = [
            'sport_id', 'gender', 'founded',
            'type', 'placeholder', 'last_played_at',
            'Unnamed: 0'
        ]
        # Mantém apenas as colunas existentes
        cols_to_drop = [c for c in remover if c in df.columns]
        return df.drop(columns=cols_to_drop)

    def add_country_season(self, raw_folder, output_folder):
        """
        Para cada CSV em raw_folder, extrai país e temporada do nome do arquivo
        e salva uma cópia em output_folder com colunas 'pais' e 'temporada'.
        """
        arquivos_csv = [f for f in os.listdir(raw_folder) if f.endswith('.csv')]
        os.makedirs(output_folder, exist_ok=True)

        for arquivo in arquivos_csv:
            match = re.search(r'([A-Za-z}]+)(\d{2}_\d{2})', arquivo)
            pais, temporada = (match.group(1), match.group(2)) if match else (None, None)

            df = pd.read_csv(os.path.join(raw_folder, arquivo))
            df['pais'] = pais
            df['temporada'] = temporada

            novo_nome = arquivo.replace('.csv', '_tratado.csv')
            caminho_saida = os.path.join(output_folder, novo_nome)
            df.to_csv(caminho_saida, index=False)

    def concat_folder(self, folder):
        """Concatena todos os CSVs de um diretório em um único DataFrame."""
        files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]
        dfs = [pd.read_csv(f) for f in files]
        return pd.concat(dfs, ignore_index=True)

    def merge_with_season_ids(self, compiled_path):
        """
        Lê o CSV compilado e faz merge com o CSV de ligas/temporadas,
        preservando ID LIGA, NOME LIGA, País, Confederação e id_temporada.
        """
        # Carrega o DataFrame compilado
        df = pd.read_csv(compiled_path)

        # Caminho para o CSV de ligas/temporadas
        liga_csv = os.path.join(self.config.DATA_FOLDER, 'id_temporada_LIGAS.csv')
        df_ligas = pd.read_csv(liga_csv)

        # Renomeia 'temporada' para 'periodo_temporada' para merge
        df_ligas = df_ligas.rename(columns={'temporada': 'periodo_temporada'})

        # Merge
        df_merged = pd.merge(
            df,
            df_ligas,
            left_on='temporada',
            right_on='periodo_temporada',
            how='left'
        )

        # Descarta coluna auxiliar
        df_merged = df_merged.drop(columns=['periodo_temporada'])
        return df_merged
