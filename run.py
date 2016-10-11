from flask import Flask, render_template, url_for, Blueprint
from auth import fb_auth

CRCRiskApp = Flask(__name__)
CRCRiskApp.config.from_object('config')
CRCRiskApp.register_blueprint(fb_auth);
#CRCRiskApp.jinja_env.variable_start_string = "[["
#CRCRiskApp.jinja_env.variable_end_string   = "]]"


@CRCRiskApp.route('/')
def homepage():
	return render_template('index.html')


if __name__ == '__main__':
	CRCRiskApp.run(debug=True)