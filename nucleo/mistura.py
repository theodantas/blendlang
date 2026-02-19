# nucleo/mistura.py
from .dicionario import DICIONARIO
import random

def misturar_frase_com_dic(frase_pt, porcentagem_ingles=50):
    """
    Substitui palavras da frase PT por EN com base no dicionário
    e na porcentagem desejada.
    """
    palavras = frase_pt.split()
    num_palavras = len(palavras)
    num_ingles = int((porcentagem_ingles / 100) * num_palavras)

    # Escolhe aleatoriamente as posições que serão traduzidas
    indices_para_traduzir = random.sample(range(num_palavras), num_ingles)

    frase_mista = []
    for i, palavra in enumerate(palavras):
        palavra_lower = palavra.lower()
        if i in indices_para_traduzir and palavra_lower in DICIONARIO:
            # mantém capitalização inicial
            traducao = DICIONARIO[palavra_lower]
            if palavra[0].isupper():
                traducao = traducao.capitalize()
            frase_mista.append(traducao)
        else:
            frase_mista.append(palavra)

    return " ".join(frase_mista)
