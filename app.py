from flask import Flask
from rutas.clientes import clientes_bp
from rutas.autos import autos_bp
from rutas.rentas import rentas_bp
from rutas.reparaciones import reparaciones_bp
from rutas.devoluciones import devoluciones_bp
from rutas.alertas import alertas_bp


app = Flask(__name__)

# Registro de rutas
app.register_blueprint(clientes_bp)
app.register_blueprint(autos_bp)
app.register_blueprint(rentas_bp)
app.register_blueprint(reparaciones_bp)
app.register_blueprint(devoluciones_bp)
app.register_blueprint(alertas_bp)

@app.route("/")
def home():
    return "API de Renta de Autos - Flask + MongoDB"

if __name__ == "__main__":
    app.run(debug=True)
