"""
Processa sequencialmente os dados CSV:
1. Processa e trata arquivos brutos
2. Compila múltiplos CSV em um único DataFrame
3. Adiciona colunas de país e temporada
4. Remove colunas indesejadas e gera dados finais
"""
import pandas as pd
from .file_handler import FileHandler

class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.file_handler = FileHandler(config)

    def process_all(self):
        # Passo 1: tratar compilado
        compiled_path = self.file_handler.get_compiled_path()
        df_compiled = self.file_handler.read_csv(compiled_path)

        df_tratado = self.file_handler.drop_columns(df_compiled)
        tratado_path = self.file_handler.get_tratado_path()
        self.file_handler.write_csv(df_tratado, tratado_path)

        # Passo 2: adicionar país e temporada aos CSV individuais
        raw_folder = self.config.INPUT_DIR
        treated_folder = self.config.TEMP_DIR
        self.file_handler.add_country_season(raw_folder, treated_folder)

        # Passo 3: compilar todos os tratados
        df_merged = self.file_handler.concat_folder(treated_folder)
        merged_path = self.file_handler.get_compiled_path()
        self.file_handler.write_csv(df_merged, merged_path)

        # Passo 4: merge com IDs de temporada e gerar dados finais
        final_df = self.file_handler.merge_with_season_ids(merged_path)
        final_path = self.file_handler.get_final_data_path()
        self.file_handler.write_csv(final_df, final_path)
        return final_df
