from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime


alertas_bp = Blueprint("alertas", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
alertas = db["alertas"]

@alertas_bp.route("/alerta", methods=["POST"])
def registrar_alerta():
    data = request.json
    data["fecha"] = datetime.now().isoformat()
    alertas.insert_one(data)
    return jsonify({"mensaje": "Alerta registrada"}), 201
