"""
Interage com a API SportMonks para gerar URLs e obter dados.
"""
import requests
from urllib.parse import urlencode

class ApiHandler:
    def __init__(self, config):
        self.token = config.API_TOKEN
        self.base_url = config.API_BASE_URL

    def build_team_url(self, team_id, season_id):
        endpoint = f"{self.base_url}/teams/{team_id}"
        params = {
            'filter': f"teamstatisticSeasons={season_id}",
            'include': 'statistics.details.type',
            'api_token': self.token
        }
        return f"{endpoint}?{urlencode(params)}"

    def fetch(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
