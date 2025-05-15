import os
from sportmonk_facilitator.config import Config
from .steps import (
    step_compile_raw,
    step_treat_compiled,
    step_add_country_season,
    step_compile_treated,
    step_merge_with_season_ids,
    step_filter_data,
    step_generate_urls,
    step_fetch_api
)
from sportmonk_facilitator.utils.path_utils import ensure_dir_exists

class Controller:
    def __init__(self):
        self.config = Config()
        # Garante que os dirs base existam
        for d in (self.config.INPUT_DIR, self.config.OUTPUT_DIR, self.config.TEMP_DIR):
            ensure_dir_exists(d)

    def run(self):
        print("🔄 Iniciando pipeline SportMonks CSV Fetcher 🔄\n")

        # 0. Valida se há CSVs em input
        input_files = [f for f in os.listdir(self.config.INPUT_DIR) if f.endswith('.csv')]
        if not input_files:
            print(f"[Erro] Não foi encontrado nenhum CSV em '{self.config.INPUT_DIR}'.")
            print("Coloque seus arquivos CSV brutos nessa pasta e execute novamente.")
            return

        # 1. Concatena raws
        step_compile_raw(self.config)
        print("✔️  CSV bruto compilado.")

        # 2. Trata CSV compilado
        step_treat_compiled(self.config)
        print("✔️  CSV compilado tratado.")

        # 3. Adiciona país e temporada
        step_add_country_season(self.config)
        print("✔️  País e temporada adicionados aos arquivos.")

        # 4. Recompila tratados
        step_compile_treated(self.config)
        print("✔️  CSV tratado recompilado.")

        # 5. Merge com IDs de temporada
        step_merge_with_season_ids(self.config)
        print("✔️  Dados finais gerados.\n")

        # 6. Pergunta ao usuário pelos filtros
        team = input("Informe o nome do time (ex: Flamengo): ").strip()
        league = input("Informe o ID da liga (ex: 1988): ").strip()
        season = input("Informe a temporada (ex: 22_23): ").strip()

        df_filtered, filtered_path = step_filter_data(self.config, team, league, season)
        print(f"✔️  Dados filtrados salvos em: {filtered_path}\n")

        # 7. Gera CSV de URLs
        df_urls, urls_path = step_generate_urls(self.config, df_filtered)
        print(f"✔️  URLs geradas em: {urls_path}\n")

        # 8. Pergunta e faz fetch à API
        json_out = os.path.join(self.config.OUTPUT_DIR, "dados_api.json")
        if step_fetch_api(urls_path, json_out):
            print(f"✔️  Respostas da API salvas em: {json_out}")
        print("\n🏁 Pipeline concluído. 🏁")
