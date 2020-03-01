from flask_restful import Resource, Api
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from service.artefact_service import artefact_service

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':"Python Flask RESTful Template"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

api = Api(app)
##dork = artefact_service('Maurilho',0.666,666,22522,'tempo local');
##print(dork.get());

api.add_resource(artefact_service, '/ArtefactMetadata')

if __name__ == '__main__':
    app.run(debug=True)
