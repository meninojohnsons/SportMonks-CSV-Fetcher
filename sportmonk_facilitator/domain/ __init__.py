"""
Classes do domínio da aplicação que representam as principais entidades de negócio.
Este módulo inicializa o pacote domain e facilita importações.
"""

from .team import Team
from .league import League
from .season import Season

__all__ = ['Team', 'League', 'Season']
