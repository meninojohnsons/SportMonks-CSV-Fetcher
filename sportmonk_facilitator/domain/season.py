"""
Define a entidade Season.
"""

class Season:
    def __init__(self, id: int, name: str, start_date: str = None, end_date: str = None):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Season id={self.id} name='{self.name}' start='{self.start_date}' end='{self.end_date}'>"
