import functools
from spotify_app.spotify_auth import SpotifyAuth
from flask import (
    Blueprint, redirect, request, session, current_app, make_response
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/get_auth')
def get_auth():

    # Scope choice can default to None
    spot_auth = SpotifyAuth(client_id=current_app.config['client_id'],
                            redirect_uri=current_app.config['redirect_uri'],
                            scope_choice=current_app.config.get('scope_choice'))

    # Holds server side state
    # TODO: Create a way of storing this state so can ensure states are the same
    spot_auth.gen_state()
    session['serv_side_state'] = spot_auth.state
    return redirect(spot_auth.start_redirect(), code=302)


# TODO: Double check this actually works
def state_match(view):
    """A check done between auth code requests to see if states match."""
    @functools.wraps(view)
    def decorated_func(**kwargs):
        if request.values['state'] != session['serv_side_state']:
            return make_response("Callback state doesn't match initial request", 400)
        return view(**kwargs)
    return decorated_func


@bp.route('/callback')
@state_match
def auth_callback():

    # Spotify sends error if improper initial request
    err = request.values.get('error')
    if err is not None:
        return f"{err}"

    session['auth_code'] = request.values['code']

    # TODO: start the next stage of the auth process
    return redirect()


@bp.route('/bad_callback')
def state_mismatch():
    return make_response("Callback state doesn't match initial request", 400)

