import os
import pandas as pd
import numpy as np
import re

pasta = r'/mnt/hd/Projetos/dadosfut/csv'

caminho_temporada = r'/mnt/hd/Projetos/dadosfut/csv_pais_temporada'

arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]

for arquivo in arquivos_csv:
    # Extrair a temporada do nome do arquivo usando regex
    match = re.search(r'([A-Za-z}]+)(\d{2}_\d{2})', arquivo)
    if match:
        pais = match.group(1)
        temporada = match.group(2)
    else:
        print(f"Aviso: Não foi possível encontrar a temporada no nome do arquivo: {arquivo}")
        temporada = None  # Ou algum valor padrão que você queira usar
        nome = None

    if pais and temporada:
        caminho_completo = os.path.join(pasta, arquivo)
        try:
            df = pd.read_csv(caminho_completo)
            df['pais'] = pais
            df['temporada'] = temporada  # Adiciona a nova coluna
            nome_base, extensao = os.path.splitext(arquivo)
            novo_nome_arquivo = f"{nome_base}_tratado2{extensao}"
            novo_caminho_completo = os.path.join(caminho_temporada, novo_nome_arquivo)
            df.to_csv(novo_caminho_completo, index=False)  # Salva o novo arquivo sem o índice
            print(f"Arquivo '{arquivo}' processado e salvo como '{novo_nome_arquivo}'")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{arquivo}': {e}")

print("Processamento de todos os arquivos concluído.")