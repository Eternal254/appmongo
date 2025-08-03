from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime


devoluciones_bp = Blueprint("devoluciones", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
devoluciones = db["devoluciones"]
rentas = db["rentas"]
autos = db["autos"]

@devoluciones_bp.route("/devolucion", methods=["POST"])
def registrar_devolucion():
    data = request.json
    data["fecha"] = datetime.now().isoformat()
    devoluciones.insert_one(data)

    # actualizar estado del auto a disponible
    renta = rentas.find_one({"_id": data["renta_id"]})
    if renta:
        autos.update_one({"_id": renta["auto_id"]}, {"$set": {"disponible": True}})
        rentas.update_one({"_id": data["renta_id"]}, {"$set": {"activa": False}})

    return jsonify({"mensaje": "Devolución registrada"}), 201
