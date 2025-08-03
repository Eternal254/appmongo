from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime


rentas_bp = Blueprint("rentas", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
rentas = db["rentas"]
autos = db["autos"]

@rentas_bp.route("/renta", methods=["POST"])
def registrar_renta():
    data = request.json
    data["fecha_inicio"] = datetime.now().isoformat()
    data["activa"] = True
    rentas.insert_one(data)
    # marcar auto como no disponible y sumar contador
    autos.update_one({"_id": data["auto_id"]}, {
        "$set": {"disponible": False},
        "$inc": {"veces_rentado": 1}
    })
    return jsonify({"mensaje": "Renta registrada"}), 201
