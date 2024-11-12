from flask import render_template


class CityService:
    @staticmethod
    def get_all_cities():
        return render_template("cities.html")

    @staticmethod
    def create_city():
        pass


class AirportService:
    @staticmethod
    def get_all_airports():
        return render_template("airports.html")


class FlightService:
    @staticmethod
    def get_all_flights(offset, max_count, sort_by, sort_order):
        return render_template("flights.html")
