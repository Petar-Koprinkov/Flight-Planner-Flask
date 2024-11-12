from app import db


class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    country = db.Column(db.String(80))
    airports = db.relationship('Airport')


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure_airport = db.Column(db.String(80))
    arrival_airport = db.Column(db.String(80))
    departure_time = db.Column(db.DateTime)
    travel_time = db.Column(db.Interval)
    price = db.Column(db.Float)
