from flask import Blueprint, request, jsonify
from pymongo import MongoClient


autos_bp = Blueprint("autos", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
autos = db["autos"]

@autos_bp.route("/auto", methods=["POST"])
def registrar_auto():
    data = request.json
    data.setdefault("disponible", True)
    data.setdefault("veces_rentado", 0)
    autos.insert_one(data)
    return jsonify({"mensaje": "Auto registrado"}), 201

@autos_bp.route("/auto", methods=["GET"])
def obtener_autos():
    resultado = list(autos.find({}, {"_id": 0}))
    return jsonify(resultado)
