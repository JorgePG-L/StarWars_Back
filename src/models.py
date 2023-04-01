from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    character = db.relationship('Charachter')

    def __init__(self, population, description, name):
        self.population =  population
        self.description = description
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "population": self.population,
            "name": self.name,
            "description": self.description,
            
        }


class Charachter(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')
    
    def __init__(self, name, description, age, homeWorld):
        self.age =  age
        self.description = description
        self.name = name
        self.homeWorld = homeWorld
    def serialize(self):
        return {
            "id": self.id,
            "age": self.age,
            "description": self.description,
            "name": self.name,
            "homeWorld": self.homeWorld,
            
            
        }
