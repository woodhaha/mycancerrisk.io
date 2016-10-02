from flask import Flask
from flask import request, jsonify, render_template
#from api import api


CRCRiskApp = Flask(__name__)

CRCRiskApp.jinja_env.variable_start_string = "[["
CRCRiskApp.jinja_env.variable_end_string   = "]]"

#CRCRiskApp.register_blueprint(form_api, url_prefix='/getTest')
#CRCRiskApp.register_blueprint(api)

@CRCRiskApp.route('/', methods=['GET'])
def homepage():
	return render_template('index.html')

if __name__ == '__main__':
	CRCRiskApp.run(debug=True)