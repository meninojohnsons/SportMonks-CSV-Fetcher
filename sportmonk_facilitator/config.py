import os
from dotenv import load_dotenv

# Carrega variáveis do .env para o ambiente
load_dotenv()

class Config:
    """Configurações globais do pacote sportmonk_csf_fetcher."""
    # Token de acesso à API SportMonks
    API_TOKEN = os.getenv("API_TOKEN")
    # URL base para chamadas à API
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.sportmonks.com/v3/football")
    # Diretórios de dados
    DATA_FOLDER = os.getenv("DATA_FOLDER", "csv")
    INPUT_DIR = os.path.join(DATA_FOLDER, "input")
    OUTPUT_DIR = os.path.join(DATA_FOLDER, "output")
    TEMP_DIR = os.path.join(DATA_FOLDER, "temp")
    # Diretório de checkpoints
    CHECKPOINT_DIR = os.getenv("CHECKPOINT_DIR", os.path.join(TEMP_DIR, "checkpoints"))
