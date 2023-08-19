import pytest
import re
from urllib.parse import urlparse


def test_gen_state(setup_spotify_auth):
    setup_spotify_auth.gen_state(state_len=10)
    assert len(setup_spotify_auth._state) == 10


@pytest.fixture
def setup_redirect_url(setup_spotify_auth):
    return urlparse(setup_spotify_auth.start_redirect())


def test_start_redirect_baseurl(setup_spotify_auth, setup_redirect_url):
    # Clean up of base URL to allow comparison with urllib parsed object
    last_slash = setup_spotify_auth._accounts_url.rfind('/')
    class_base_url = setup_spotify_auth._accounts_url[last_slash+1:]

    assert setup_redirect_url.netloc == class_base_url


def test_start_redirect_qparams(setup_spotify_auth, setup_redirect_url):
    test_values = [setup_spotify_auth.client_id, setup_spotify_auth.redirect_uri]

    # Cleanup of urlparse return object
    q_param_lis = re.split("[&=]", setup_redirect_url.query)
    assert set(test_values).issubset(q_param_lis)


def test_start_redirect_qparams_wstate(setup_spotify_auth):
    setup_spotify_auth._state = 'state'
    new_parsed_url = urlparse(setup_spotify_auth.start_redirect())

    test_values = [setup_spotify_auth.client_id, setup_spotify_auth.redirect_uri, setup_spotify_auth._state]

    # Cleanup of urlparse return object
    q_param_lis = re.split("[&=]", new_parsed_url.query)
    assert set(test_values).issubset(q_param_lis)


def test_start_redirect_qparams_scope_choice(setup_spotify_auth):
    setup_spotify_auth.scope_choice.extend(['test_scope_choice2', 'test_scope_choice3'])
    test_values = [setup_spotify_auth.client_id, setup_spotify_auth.redirect_uri] + setup_spotify_auth.scope_choice

    new_parsed_url = urlparse(setup_spotify_auth.start_redirect())

    # Cleanup of urlparse return object
    q_param_lis = re.split("[&=+]", new_parsed_url.query)
    assert set(test_values).issubset(q_param_lis)