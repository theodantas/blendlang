# app.py
from flask import Flask, render_template, request, jsonify
from nucleo.conexao_planilha import conectar_planilha, atualizar_vezes_usada
from nucleo.carregar_frases import sortear_frase
from nucleo.mistura import misturar_frase_com_dic
import os

app = Flask(__name__)

def normalizar_texto(texto):
    return texto.strip().lower()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gerar", methods=["POST"])
def gerar_frase():
    categoria = request.form.get("categoria")
    nivel = request.form.get("nivel")
    porcentagem = int(request.form.get("porcentagem"))

    aba = conectar_planilha()
    frase_info = sortear_frase(aba, categoria, nivel)

    if not frase_info:
        return jsonify({"erro": "Nenhuma frase encontrada"})

    frase_id = frase_info["id"]
    frase_pt = frase_info["texto_pt"]
    
    atualizar_vezes_usada(aba, frase_id)

    frase_mista = misturar_frase_com_dic(frase_pt, porcentagem)

    return jsonify({
        "frase": frase_mista,
        "resposta_correta": frase_pt
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)