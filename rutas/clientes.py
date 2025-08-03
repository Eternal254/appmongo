from flask import Blueprint, request, jsonify
from pymongo import MongoClient


clientes_bp = Blueprint("clientes", __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["renta_autos"]
clientes = db["clientes"]

@clientes_bp.route("/cliente", methods=["POST"])
def crear_cliente():
    data = request.json
    clientes.insert_one(data)
    return jsonify({"mensaje": "Cliente registrado"}), 201

@clientes_bp.route("/cliente", methods=["GET"])
def obtener_clientes():
    resultado = list(clientes.find({}, {"_id": 0}))
    return jsonify(resultado)
