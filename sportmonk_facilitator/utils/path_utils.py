import os

def ensure_dir_exists(path):
    """
    Garante que o diretório do caminho fornecido exista.
    """
    os.makedirs(path, exist_ok=True)
