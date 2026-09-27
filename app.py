from flask import  Flask, render_template, jsonify
from dotenv import load_dotenv
from services.clima import clima_local

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/clima-local/<cidade>")
def pegar_clima(cidade):
    dados = clima_local(cidade)
    return jsonify(dados)


if __name__ == "__main__":
    app.run(debug=True)

