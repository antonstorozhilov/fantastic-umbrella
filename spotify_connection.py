from datetime import datetime, timedelta
import os
import requests

class SpotifyConnection():
    def __init__(self):
        self._token_expiry_time = None
        self._token = None

    def _token_refresh(self) -> None:
        if (self._token is not None) and (datetime.now() < self._token_expiry_time):
            return
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": os.getenv('SPOTIFY_CLIENT'),
            "client_secret": os.getenv('SPOTIFY_SECRET')
        }

        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
        if (response.status_code == 200):
            response_data = response.json()
            self._token = response_data.get('access_token')
            self._token_expiry_time = datetime.now() + timedelta(seconds=(response_data.get('expires_in')-10))
            print("Successfully retrieved access token.")
        else:
            print("Failed to get auth token. ", response.status_code, response.text)
     

    def get_artist_data(self, artist_id) -> dict:
        self._token_refresh()

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}', headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed request to get artist data. ", response.status_code, response.text)