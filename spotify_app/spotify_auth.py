import random
import string

class SpotifyAuth:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope_choice: str):
        _accounts_url = 'https://accounts.spotify.com'
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope_choice = scope_choice
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self):
        self._state = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=30))

    def start_redirect(self, show_dialog=False):
