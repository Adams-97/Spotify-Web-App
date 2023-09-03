import pytest
from spotify_app.spotify_auth import SpotifyAuth


# Create test spotify auth class for use by all tests
@pytest.fixture(scope='module')
def setup_spotify_auth():
    return SpotifyAuth('test_client_id', 'test_client_secret', 'test_redirect_uri', ['test_scope_choice'])

