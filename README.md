# SportMonk API Data Facilitator

## Visão Geral
Este projeto facilita a recuperação e tratamento de dados da API SportMonk para análises esportivas. Desenvolvido como parte de um artigo acadêmico, o sistema automatiza o processo de coleta, tratamento e organização de dados de diferentes ligas de futebol de todo o mundo.

## Estrutura do Projeto
O projeto consiste em uma série de scripts Python que trabalham em conjunto para:
1. Extrair dados de arquivos CSV
2. Adicionar informações de país e temporada
3. Compilar os dados em um único arquivo
4. Enriquecer os dados com IDs de temporada
5. Gerar URLs para consulta à API SportMonk
6. Fazer requisições à API e armazenar as respostas

## Requisitos
- Python 3.6+
- Bibliotecas Python:
  - pandas
  - numpy
  - requests
  - csv
  - json
  - re (expressões regulares)

Instale as dependências com:
```bash
pip install pandas numpy requests
```

## Scripts e Fluxo de Trabalho

### 1. `colocar_pais_temporada.py`
Adiciona colunas de país e temporada aos arquivos CSV com base no nome do arquivo.

```python
# Exemplo de uso
# O script processa arquivos no formato {PAIS}{TEMPORADA}.csv
# Ex: Italia10_11.csv, Brasil22_23.csv
python colocar_pais_temporada.py
```

### 2. `compilar_arquivo.py`
Combina todos os arquivos CSV tratados em um único arquivo compilado.

```python
# Exemplo de uso
python compilar_arquivo.py
# Gera o arquivo times_compilados.csv
```

### 3. `tratar_compilado.py`
Remove colunas desnecessárias do arquivo compilado.

```python
# Exemplo de uso
python tratar_compilado.py
# Gera o arquivo times_compilados_tratados.csv
```

### 4. `id_na_tabela_tratada.py`
Adiciona IDs de temporada ao arquivo tratado baseado no mapeamento do arquivo `id_temporada - LIGAS.csv`.

```python
# Exemplo de uso
python id_na_tabela_tratada.py
# Gera o arquivo dados_finais.csv
```

### 5. `requisição2.py`
Gera URLs para consultas na API SportMonk baseado nos IDs dos times e temporadas.

```python
# Exemplo de uso
python requisição2.py
# Gera o arquivo urls_api_sportmonks_por_time.csv
```

### 6. `script.py`
Executa as requisições à API SportMonk utilizando as URLs geradas e salva os resultados em um arquivo JSON.

```python
# Exemplo de uso
python script.py urls_api_sportmonks_por_time.csv resultados_api.json
```

## Fluxo de Dados

```
Arquivos CSV originais 
      ↓
colocar_pais_temporada.py (adiciona país e temporada)
      ↓
compilar_arquivo.py (combina todos os arquivos)
      ↓
tratar_compilado.py (remove colunas desnecessárias)
      ↓
id_na_tabela_tratada.py (adiciona IDs de temporada)
      ↓
requisição2.py (gera URLs de API)
      ↓
script.py (faz requisições à API e salva resultados)
```

## Estrutura de Arquivos
- `id_temporada - LIGAS.csv`: Arquivo de mapeamento que relaciona temporadas com seus respectivos IDs.
- `times_compilados.csv`: Resultado da compilação de todos os arquivos CSV tratados.
- `times_compilados_tratados.csv`: Arquivo compilado após remoção de colunas desnecessárias.
- `dados_finais.csv`: Dados tratados com IDs de temporada incluídos.
- `urls_api_sportmonks_por_time.csv`: Lista de URLs para consulta à API.
- `resultados_api.json`: Resultados das consultas à API.

## Personalização da API

Para usar sua própria chave de API SportMonk, modifique a variável `base_url` no arquivo `requisição2.py`:

```python
base_url = "https://api.sportmonks.com/v3/football/teams/{id}?filter=teamstatisticSeasons={id_temporada}&include=statistics.details.type&api_token=SUA_API_KEY"
```

## Exemplo de Uso Completo

```bash
# 1. Processar os arquivos CSV originais
python colocar_pais_temporada.py

# 2. Compilar os arquivos tratados
python compilar_arquivo.py

# 3. Tratar o arquivo compilado
python tratar_compilado.py

# 4. Adicionar IDs de temporada
python id_na_tabela_tratada.py

# 5. Gerar URLs para API
python requisição2.py

# 6. Fazer requisições à API
python script.py urls_api_sportmonks_por_time.csv resultados_api.json
```

## Contribuições
Este projeto foi desenvolvido como parte de um artigo acadêmico, mas está disponível para uso da comunidade. Contribuições são bem-vindas através de pull requests.

## Autores
- [Davi Moreira Fuzatto]
- [João Gabriel de Paula Costa Dias]

## Licença
Este projeto está licenciado sob [MIT License].

## Notas
- Este projeto é independente e não é afiliado oficialmente à SportMonk.
- Respeite os termos de uso da API SportMonk ao utilizar este código.
