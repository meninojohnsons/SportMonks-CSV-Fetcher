# SportMonks CSV Fetcher

Um utilitário em python que cria arquivos .csv com urls tradadas para api, lê as urls, executa as requisições HTTP GET e salva em um único arquivo JSON com estatística de diferentes temporadas de times de futebol. 

## Funcionalidades
- Lê automaticamente todas as URLs da coluna url em um arquivo CSV com cabeçalho.

- Executa requisições às URLs (que já incluem o parâmetro api_token).

- Trata falhas isoladas sem interromper o processamento completo.

- Agrega todas as respostas JSON em uma lista e salva num arquivo output.json com formatação legível.

## Pré-requisitos
- Python 3.6 ou superior
- Biblioteca `requests`
```bash
pip install requests
```

## Uso
1. Prepare um CSV (`urls.csv`) no formato:
```
pais,temporada,team_id,url
UK,18_19,1,https://api.sportmonks.com/v3/football/teams/1?…&api_token=SEU_TOKEN
UK,19_20,1,https://api.sportmonks.com/v3/football/teams/1?…&api_token=SEU_TOKEN
```
2. Clone o reposiório e instale depências:
```bash
git clone https://github.com/SEU_USUARIO/sportmonks-csv-fetcher.git
cd sportmonks-csv-fetcher
pip install -r requirements.txt
```
3. Execute o script:
```bash
python fetcher.py urls.csv output.json 
```
4. Os dados agregados estarão em `output.json`
## Estrutura do Projeto
```
.
├── fetcher.py        # Script principal
├── requirements.txt  # dependências do projeto
└── urls.csv          # exemplo de arquivo de URLs
```
## Possíveis melhorias
- log de erros detalhado em arquivo separado.
- Suporte a pagination automática para endpoints SportMonks
- Exportação para CSV ou banco de dados.

