from flask import Flask, request, jsonify, render_template, url_for, session, redirect
#from api import api
from flask_oauthlib.client import OAuth, OAuthException

FACEBOOK_APP_ID = '1644776055813210'
FACEBOOK_APP_SECRET = '8d9d8d1aa06c8b3817e2d1bbca21e8b2'

CRCRiskApp = Flask(__name__)
CRCRiskApp.debug = True
CRCRiskApp.secret_key = 'development'
oauth = OAuth(CRCRiskApp)

CRCRiskApp.jinja_env.variable_start_string = "[["
CRCRiskApp.jinja_env.variable_end_string   = "]]"

facebook = oauth.remote_app(
    'facebook',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    access_token_method='GET',
    authorize_url='https://www.facebook.com/dialog/oauth'
)


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

def pop_login_session():
#    session.pop('logged_in', None)
 #   session.pop('facebook_token', None)
    session.clear()

@CRCRiskApp.route('/')
def homepage():
	return render_template('index.html')

@CRCRiskApp.route('/login')
def login():
    callback = url_for(
        'facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return facebook.authorize(callback=callback)


@CRCRiskApp.route('/login/authorized')
def facebook_authorized():
    resp = facebook.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['oauth_token'] = (resp['access_token'], '')
    session['logged_in'] = True

    me = facebook.get('/me') # get user info (id, uname)

    return redirect(url_for('homepage'))

@CRCRiskApp.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
	CRCRiskApp.run(debug=True)