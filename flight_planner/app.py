from flask import Flask
from flight_planner.routes import register_routes
from flask_sqlalchemy import SQLAlchemy
from  os import path

db = SQLAlchemy()
DB_NAME = "flight_planner.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Petar Koprinkov'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    register_routes(app)

    from models import City, Airport, Flight
    create_database(app)

    return app


def create_database(app):
    with app.app_context():
        if not path.exists('flight_planner/' + DB_NAME):
            db.create_all()
            print('Created Database!')


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
