import random
import string
from urllib.parse import urlencode
from typing import Optional


class SpotifyAuth:
    """An abstraction for authentication handling with Spotify API.

    Attributes:
        client_id (str): client_id given by Spotify
        client_secret (str): client_secret given by Spotify
        redirect_uri (str): URL that Spotify redirects to after user login
        scope_choice (list): List of all scope choices chosen for session

    """

    # Base URL needed for authorisation
    _accounts_url = 'https://accounts.spotify.com'

    def __init__(self, client_id: str, redirect_uri: str, scope_choice: Optional[list[str]] = None):
        self._state = None
        self.client_id = client_id
        # self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope_choice = scope_choice

    def gen_state(self, state_len: int = 30):
        """Generates a state that can be passed between requests

        Args:
            (int): Len of string generated

        Returns:
            (str): Random sequence of characters
        """

        # Generate random 30 character string to identify requests/responses
        self._state = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=state_len))

    def start_redirect(self, show_dialog=False):
        """Prepares the URL to start Spotify auth process with user

        Args:
            show_dialog (bool): Optional parameter that forces the user to approve the app again instead of redirected

        Returns:
            (str): URL encoded string which starts authorisation
        """

        # State, show_dialog and scope are optional parameters for the initial request
        query_params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'show_dialog': show_dialog
        }

        if self.scope_choice is not None:
            query_params['scope'] = ' '.join(self.scope_choice)

        if self._state is not None:
            query_params['state'] = self._state

        return self._accounts_url + '?' + urlencode(query_params)