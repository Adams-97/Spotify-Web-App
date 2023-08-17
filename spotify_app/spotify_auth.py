import random
import string


class SpotifyAuth:
    """An abstraction for authentication handling with Spotify API.

    Attributes:
        client_id (str): client_id given by Spotify
        client_secret (str): client_secret given by Spotify
        redirect_uri (str): URL that Spotify redirects to after user login
        scope_choice (list):

    """
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope_choice: list):
        _accounts_url = 'https://accounts.spotify.com'
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope_choice = scope_choice

        # Generate random 30 character string to identify requests/responses
        self._state = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=30))

    @property
    def state(self):
        return self._state

    def start_redirect(self, show_dialog=False):
        pass
