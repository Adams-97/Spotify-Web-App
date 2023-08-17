import pytest


def test_state_set(setup_spotify_auth):
    assert len(setup_spotify_auth._state) == 30


def test_state_change(setup_spotify_auth):
    with pytest.raises(AttributeError) as err:
        setup_spotify_auth.state = 'Changed state code'