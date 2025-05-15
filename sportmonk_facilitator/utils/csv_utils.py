import csv
import json
import sys
import requests

def fetch_and_store_from_csv(csv_file, output_file):
    """
    Lê URLs da coluna 'url' de um CSV e faz requisições, salvando todas as respostas num único JSON.
    """
    aggregated = []

    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if 'url' not in reader.fieldnames:
                print(f"[Erro] Coluna 'url' não encontrada no CSV. Colunas disponíveis: {reader.fieldnames}")
                sys.exit(1)
            for row in reader:
                url = row['url'].strip()
                if not url:
                    continue
                print(f"Requisitando: {url}")
                try:
                    resp = requests.get(url)
                    resp.raise_for_status()
                    aggregated.append(resp.json())
                except requests.RequestException as e:
                    print(f"  → Falha ao requisitar {url}: {e}")
    except FileNotFoundError:
        print(f"[Erro] Arquivo {csv_file} não encontrado.")
        sys.exit(1)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(aggregated, f, ensure_ascii=False, indent=2)

    print(f"Dados salvos em {output_file}")
