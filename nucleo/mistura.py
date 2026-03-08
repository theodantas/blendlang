# nucleo/mistura.py
from .dicionario import DICIONARIO
import random

def misturar_frase_com_dic(frase_pt, porcentagem_ingles=50):
    palavras = frase_pt.split()

    # Descobrir quais palavras existem no dicionário
    palavras_tradutiveis = [
        i for i, palavra in enumerate(palavras)
        if palavra.lower() in DICIONARIO
    ]

    if not palavras_tradutiveis:
        return frase_pt

    # Calcular quantas traduzir com base nas tradutíveis
    num_tradutiveis = len(palavras_tradutiveis)
    num_ingles = int((porcentagem_ingles / 100) * num_tradutiveis)

    num_ingles = min(num_ingles, num_tradutiveis)

    indices_para_traduzir = random.sample(palavras_tradutiveis, num_ingles)

    frase_mista = []

    for i, palavra in enumerate(palavras):
        palavra_lower = palavra.lower()

        if i in indices_para_traduzir:
            traducao = DICIONARIO[palavra_lower]

            if palavra[0].isupper():
                traducao = traducao.capitalize()

            frase_mista.append(traducao)
        else:
            frase_mista.append(palavra)

    return " ".join(frase_mista)