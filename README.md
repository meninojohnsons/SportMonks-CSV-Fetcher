# SportMonks CSV Fetcher
### Versão 0.1.1 
Uma ferramenta em Python que facilita o acesso e processamento de dados da API SportMonks, permitindo a compilação, tratamento e análise de dados em arquivos CSV e JSON.

## ✅ Funcionalidades
- ✅ Criação automatizada de CSVs com URLs personalizadas da API SportMonks.

- ✅ Requisições HTTP com tratamento de falhas e coleta de dados agregados.

- ✅ Salvamento em `output.json` com formatação legível.

- ✅ Pipeline completa com múltiplas etapas:

- ✅ Compilação de CSV bruto.

- ✅ Tratamento e filtragem de dados.

- ✅ Inclusão de país, temporada, ID da liga e outras colunas.

- ✅ Interface interativa para selecionar time, liga e temporada.

- ✅ Script de configuração (`setup.py`) com criação automática de pastas e arquivo `.env`.

## ⚙️ Instalação
### Pré-requisitos
- Python 3.7 ou superior
- `pip`
- Recomendado: usar um ambiente virtual
```bash
python -m venv .venv       #Primeiro execute esse

source .venv/bin/activate  # Linux/macOS

.venv\Scripts\activate     # Windows
```

### Instalação do Pacote
```bash
pip install -r requirements.txt
```

## 🚀 Configuração Inicial
Antes de executar o programa, rode o script de configuração:
```bash
python initialize.py
```
O que será feito:
- Criação das pastas necessárias:
- `csv/input`
- `csv/output`
- `csv/temp`
- Criação do arquivo `.env` com seu token da API:
```
API_TOKEN=seu_token_aqui
```

## Como executar
Após configurar o projeto:
```bash
python main.py
```
Durante a execução,você será solicitado a informar:
- nome do time
- ID da liga(ex:271)
- Temporada(ex:22_23)
O programa executará a pipeline completa e salvará os dados no diretório `csv/output`.

## 🗂️ Estrutura do Projeto

```graphql
.
├── csv/
│   ├── input/      # Arquivos CSV brutos
│   ├── output/     # Saídas finais processadas
│   └── temp/       # Arquivos intermediários
├── sportmonk_facilitator/
│   └── ...         # Pacote com os módulos da pipeline
├── main.py         # Ponto de entrada da aplicação
├── setup.py        # Script de instalação e configuração
├── requirements.txt
└── README.md
```
## Exemplo de Saida
Exemplo de CSV com URLs:
```csv
pais,temporada,team_id,url
UK,22_23,1,https://api.sportmonks.com/v3/football/teams/1?api_token=SEU_TOKEN
```

## 👥 Autores
- [Davi Moreira Fuzatto](https://github.com/davimf721)
- [João Gabriel de Paula Costa Dias](https://github.com/meninojohnsons)

## Contribuições
Este projeto foi desenvolvido como parte de um artigo acadêmico, mas está disponível para uso da comunidade. Contribuições são bem-vindas através de pull requests.
## Licença
Este projeto está licenciado sob [MIT License](LICENSE).

## Notas
- Este projeto é independente e não é afiliado oficialmente à SportMonk.
- Respeite os termos de uso da API SportMonk ao utilizar este código.
