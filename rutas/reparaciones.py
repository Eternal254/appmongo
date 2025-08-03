from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime


reparaciones_bp = Blueprint("reparaciones", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
reparaciones = db["reparaciones"]

@reparaciones_bp.route("/reparacion", methods=["POST"])
def registrar_reparacion():
    data = request.json
    data["fecha"] = datetime.now().isoformat()
    reparaciones.insert_one(data)
    return jsonify({"mensaje": "Reparación registrada"}), 201
