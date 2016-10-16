from flask import Flask, render_template, url_for, Blueprint, jsonify
from auth import fb_auth
from dbmongo import form_db

CRCRiskApp = Flask(__name__)
CRCRiskApp.config.from_object('config')
CRCRiskApp.register_blueprint(fb_auth);
CRCRiskApp.register_blueprint(form_db);
#CRCRiskApp.jinja_env.variable_start_string = "[["
#CRCRiskApp.jinja_env.variable_end_string   = "]]"


@CRCRiskApp.route('/')
def homepage():
	return render_template('index.html')


if __name__ == '__main__':
	CRCRiskApp.run(debug=True)