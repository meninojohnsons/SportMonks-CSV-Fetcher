"""
Define a entidade League.
"""

class League:
    def __init__(self, id: int, name: str, country: str = None, season_ids: list = None):
        self.id = id
        self.name = name
        self.country = country
        self.season_ids = season_ids or []

    def __repr__(self):
        return f"<League id={self.id} name='{self.name}' country='{self.country}' seasons={self.season_ids}>"
