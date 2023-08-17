import pytest
from spotify_app.spotify_auth import SpotifyAuth


@pytest.fixture(scope='module')
def setup_spotify_auth():
    return SpotifyAuth('client_id', 'client_secret', 'redirect_uri', ['scope_choice'])