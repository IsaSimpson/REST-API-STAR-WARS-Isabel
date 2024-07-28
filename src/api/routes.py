"""
This module takes care of starting the API Server, Loading the DB, and Adding the endpoints.
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_cors import CORS
from api.models import db, People, Planet, User, FavoritePeople, FavoritePlanet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the Google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    result = [p.serialize() for p in people]
    return jsonify(result), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
    if person:
        return jsonify(person.serialize()), 200
    return jsonify({"error": "Person not found"}), 404

@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    result = [p.serialize() for p in planets]
    return jsonify(result), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return jsonify(planet.serialize()), 200
    return jsonify({"error": "Planet not found"}), 404

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [u.serialize() for u in users]
    return jsonify(result), 200

@api.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Here you should implement the logic to get the current user
    # Currently, there's no authentication system, so this is just a basic example
    user_id = 1  # Assume the current user has ID 1
    fav_people = FavoritePeople.query.filter_by(user_id=user_id).all()
    fav_planets = FavoritePlanet.query.filter_by(user_id=user_id).all()
    result = {
        "people": [fp.people_id for fp in fav_people],
        "planets": [fp.planet_id for fp in fav_planets]
    }
    return jsonify(result), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = 1  # Assume the current user has ID 1
    favorite = FavoritePlanet(user_id=user_id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite planet added"}), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user_id = 1  # Assume the current user has ID 1
    favorite = FavoritePeople(user_id=user_id, people_id=people_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite person added"}), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = 1  # Assume the current user has ID 1
    favorite = FavoritePlanet.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite planet deleted"}), 200
    return jsonify({"error": "Favorite planet not found"}), 404

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user_id = 1  # Assume the current user has ID 1
    favorite = FavoritePeople.query.filter_by(user_id=user_id, people_id=people_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite person deleted"}), 200
    return jsonify({"error": "Favorite person not found"}), 404
