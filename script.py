import requests
import json
import csv
import sys

def fetch_and_store_from_csv(csv_file, output_file):
    """
    Lê URLs da coluna 'url' de um CSV com cabeçalho,
    faz as requisições e salva todas as respostas num único arquivo JSON.
    As URLs já devem conter o api_token no final.
    """
    aggregated = []

    # Usa DictReader para pular o cabeçalho e acessar pela chave 'url'
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if 'url' not in reader.fieldnames:
            print(f"Erro: coluna 'url' não encontrada no CSV. Colunas disponíveis: {reader.fieldnames}")
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
                # Registra erro mas continua
                print(f"  → Falha ao requisitar {url}: {e}")

    # Grava o JSON agregado
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(aggregated, f, ensure_ascii=False, indent=2)
    print(f"Dados salvos em {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <urls.csv> <ARQUIVO_SAIDA.json>")
        sys.exit(1)

    csv_path = sys.argv[1]
    saída    = sys.argv[2]
    fetch_and_store_from_csv(csv_path, saída)