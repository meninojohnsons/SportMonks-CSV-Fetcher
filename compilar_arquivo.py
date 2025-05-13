import pandas as pd
import os
import csv

pasta = r'/mnt/hd/Projetos/dadosfut/csv_pais_temporada'

arquivos = [os.path.join(pasta, caminho)for caminho in os.listdir(pasta)]

tabela_final = pd.DataFrame()

for caminho in arquivos:

    df = pd.read_csv(caminho)

    tabela_final = pd.concat([tabela_final, df])

tabela_final.to_csv('times_compilados.csv')