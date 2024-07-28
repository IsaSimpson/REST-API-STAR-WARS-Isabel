from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    favorite_people = db.relationship('FavoritePeople', backref='user', lazy=True)
    favorite_planets = db.relationship('FavoritePlanet', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    height = db.Column(db.String(64))
    mass = db.Column(db.String(64))
    hair_color = db.Column(db.String(64))
    skin_color = db.Column(db.String(64))
    eye_color = db.Column(db.String(64))
    birth_year = db.Column(db.String(64))
    gender = db.Column(db.String(64))

    favorites = db.relationship('FavoritePeople', backref='people', lazy=True)

    def __repr__(self):
        return f'<People {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    diameter = db.Column(db.String(64))
    rotation_period = db.Column(db.String(64))
    orbital_period = db.Column(db.String(64))
    gravity = db.Column(db.String(64))
    population = db.Column(db.String(64))
    climate = db.Column(db.String(64))
    terrain = db.Column(db.String(64))
    surface_water = db.Column(db.String(64))

    favorites = db.relationship('FavoritePlanet', backref='planet', lazy=True)

    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }

class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

    def __repr__(self):
        return f'<FavoritePeople {self.user_id} {self.people_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)

    def __repr__(self):
        return f'<FavoritePlanet {self.user_id} {self.planet_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
