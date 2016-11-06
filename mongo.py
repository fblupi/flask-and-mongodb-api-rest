# mongo.py

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /star to /star/

mongo = PyMongo(app)

class Star(Resource):
    def get(self, name):
        star = mongo.db.stars
        s = star.find_one({'name' : name})
        if s:
            output = {'name' : s['name'], 'distance' : s['distance']}
        else:
            output = "No such name"
        return jsonify({'result' : output})

class StarList(Resource):
    def get(self):
        star = mongo.db.stars
        output = []
        for s in star.find():
            output.append({'name' : s['name'], 'distance' : s['distance']})
        return jsonify({'result' : output})

    def post(self):
        star = mongo.db.stars
        name = request.json['name']
        distance = request.json['distance']
        star_id = star.insert({'name': name, 'distance': distance})
        new_star = star.find_one({'_id': star_id })
        output = {'name' : new_star['name'], 'distance' : new_star['distance']}
        return jsonify({'result' : output})

api.add_resource(StarList, '/star')
api.add_resource(Star, '/star/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
