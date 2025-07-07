from flask import Blueprint, request, jsonify
from models import db, Plant

# Blueprint for plants
plants_bp = Blueprint('plants', __name__)

# PATCH /plants/:id — Update is_in_stock or other fields
@plants_bp.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    # You can allow other fields to be updated too if desired
    if "name" in data:
        plant.name = data["name"]
    if "image" in data:
        plant.image = data["image"]
    if "price" in data:
        plant.price = data["price"]

    db.session.commit()

    return jsonify({
        "id": plant.id,
        "name": plant.name,
        "image": plant.image,
        "price": plant.price,
        "is_in_stock": plant.is_in_stock
    }), 200


# DELETE /plants/:id — Delete a plant
@plants_bp.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)

    db.session.delete(plant)
    db.session.commit()

    return '', 204
