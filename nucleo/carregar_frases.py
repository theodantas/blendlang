# nucleo/carregar_frases.py
import random

def carregar_frases_filtradas(aba, categoria=None, nivel=None):
    """
    Lê todas as frases e aplica filtros opcionais.
    """
    dados = aba.get_all_records()

    frases = [
        d for d in dados
        if d["status"] == "ativa"
    ]

    if categoria:
        frases = [f for f in frases if f["categoria"].lower() == categoria.lower()]

    if nivel:
        frases = [f for f in frases if f["nivel"].lower() == nivel.lower()]

    return frases


def sortear_frase(aba, categoria=None, nivel=None):
    frases = carregar_frases_filtradas(aba, categoria, nivel)

    if not frases:
        return None

    frases.sort(key=lambda x: x["vezes_usada"])
    menor_uso = frases[0]["vezes_usada"]

    candidatos = [f for f in frases if f["vezes_usada"] == menor_uso]

    return random.choice(candidatos)
