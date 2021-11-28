from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
app = Flask(__name__)
api = Api(app)

class GetTime(Resource):
    def get(self):
        time = datetime.now()
        return {'time': str(time)}

api.add_resource(GetTime, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)