import os
import json

class Checkpoint:
    """
    Gerencia um arquivo de checkpoint simples para persistir estado entre etapas.
    """
    def __init__(self, path):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def save(self, data: dict):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self) -> dict:
        if not os.path.exists(self.path):
            return {}
        with open(self.path, encoding='utf-8') as f:
            return json.load(f)

    def exists(self) -> bool:
        return os.path.exists(self.path)
