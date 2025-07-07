#!/usr/bin/env python3

from app import app
from models import db, Plant

if __name__ == '__main__':
    with app.app_context():
        # Retrieve a plant by ID
        plant = Plant.query.get(1)
        print("Before PATCH:", plant.is_in_stock)

        # Simulate PATCH
        plant.is_in_stock = False
        db.session.commit()

        # Confirm update
        updated = Plant.query.get(1)
        print("After PATCH:", updated.is_in_stock)

        # Simulate DELETE
        plant_to_delete = Plant.query.get(2)
        if plant_to_delete:
            db.session.delete(plant_to_delete)
            db.session.commit()
            print("Deleted plant with ID 2")

        # Enter interactive shell
        import ipdb; ipdb.set_trace()
