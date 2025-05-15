# sportmonk_facilitator/pipeline/steps.py

import os
import pandas as pd

from sportmonk_facilitator.data import FileHandler, ApiHandler
from sportmonk_facilitator.utils import fetch_and_store_from_csv
from sportmonk_facilitator.utils.path_utils import ensure_dir_exists

def step_compile_raw(config):
    """Concatena todos os CSV brutos em times_compilados.csv."""
    # Valida existência
    if not os.path.isdir(config.INPUT_DIR):
        raise FileNotFoundError(f"Diretório de input não encontrado: {config.INPUT_DIR}")

    raw_files = [f for f in os.listdir(config.INPUT_DIR) if f.endswith('.csv')]
    if not raw_files:
        raise FileNotFoundError(f"Nenhum CSV em: {config.INPUT_DIR}")

    fh = FileHandler(config)
    df = fh.concat_folder(config.INPUT_DIR)

    out = fh.get_compiled_path()
    ensure_dir_exists(os.path.dirname(out))
    fh.write_csv(df, out)
    return out

def step_treat_compiled(config):
    """Remove colunas indesejadas de times_compilados.csv."""
    fh = FileHandler(config)
    path_in = fh.get_compiled_path()
    df = fh.read_csv(path_in)
    df2 = fh.drop_columns(df)
    out = fh.get_tratado_path()
    ensure_dir_exists(os.path.dirname(out))
    fh.write_csv(df2, out)
    return out


def step_add_country_season(config):
    """Adiciona colunas 'pais' e 'temporada' aos CSV individuais."""
    fh = FileHandler(config)
    raw = config.INPUT_DIR
    temp = config.TEMP_DIR
    fh.add_country_season(raw, temp)
    return temp


def step_compile_treated(config):
    """Concatena todos os CSV tratados em um único DataFrame."""
    fh = FileHandler(config)
    df = fh.concat_folder(config.TEMP_DIR)
    out = fh.get_compiled_path()
    fh.write_csv(df, out)
    return out


def step_merge_with_season_ids(config):
    """Faz merge com IDs de temporada para gerar dados_finais.csv."""
    fh = FileHandler(config)
    out = fh.get_final_data_path()
    df = fh.merge_with_season_ids(fh.get_compiled_path())
    ensure_dir_exists(os.path.dirname(out))
    fh.write_csv(df, out)
    return out


def step_filter_data(config, team_name, league_id, season_str):
    """
    Filtra dados_finais.csv por nome do time, liga e temporada.
    Retorna DataFrame e caminho do CSV filtrado.
    """
    fh = FileHandler(config)
    final_csv = fh.get_final_data_path()
    df = fh.read_csv(final_csv)
    filtered = df[
        (df['name'].str.lower() == team_name.lower()) &
        (df['ID LIGA'] == int(league_id)) &
        (df['temporada'] == season_str)
    ]
    
    out = os.path.join(config.OUTPUT_DIR, f"filtered_{team_name}_{league_id}_{season_str}.csv")
    ensure_dir_exists(config.OUTPUT_DIR)
    fh.write_csv(filtered, out)
    return filtered, out


def step_generate_urls(config, df_filtered):
    """
    Gera CSV de URLs da API para cada time/temporada/pais no DataFrame filtrado.
    """
    api = ApiHandler(config)
    urls = []
    for _, row in df_filtered.drop_duplicates(subset=['id', 'temporada', 'pais']).iterrows():
        urls.append({
            'pais': row['pais'],
            'temporada': row['temporada'],
            'team_id': row['id'],
            'url': api.build_team_url(row['id'], row['id_temporada'])
        })
    df_urls = pd.DataFrame(urls)
    path = os.path.join(config.OUTPUT_DIR, "urls_api_sportmonks_por_time.csv")
    ensure_dir_exists(config.OUTPUT_DIR)
    df_urls.to_csv(path, index=False)
    return df_urls, path


def step_fetch_api(csv_path, output_json):
    """
    Pergunta ao usuário se quer fazer as requisições e, em caso afirmativo,
    usa o utilitário para gravar em JSON.
    """
    resp = input("Deseja fazer as requisições para as URLs geradas e salvar em JSON? (s/n): ").strip().lower()
    if resp == 's':
        fetch_and_store_from_csv(csv_path, output_json)
        return True
    print("Pulando requisições à API.")
    return False
