import os
import requests


class TMDBApi:
    def __init__(self):
        self._api_url = os.getenv('API_URL')
        self._api_key = os.getenv('API_KEY')

    def get_movies(self, query, page):
        """
        Get movies by search query
        :param query: string
        :param page: int
        :return: results, total_pages
        """
        try:
            res = requests.get('{}/search/movie?query={}&page='.format(self._api_url, query, page), headers=self.get_authorization_header())
            data = res.json()

            return data['results'], data['total_pages']
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as error:
            print(error)

    def get_authorization_header(self):
        """
        Get authorization header
        :return: authorization_header
        """
        return {
            'Authorization': 'Bearer {}'.format(self._api_key)
        }
