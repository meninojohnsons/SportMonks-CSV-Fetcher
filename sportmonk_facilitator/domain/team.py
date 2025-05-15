"""
Define a entidade Team.
"""

class Team:
    def __init__(self, id: int, name: str, country: str = None):
        self.id = id
        self.name = name
        self.country = country

    def __repr__(self):
        return f"<Team id={self.id} name='{self.name}' country='{self.country}'>"

