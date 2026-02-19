# nucleo/carregar_frases.py
import random

def carregar_frases_atualizadas(aba):
    """
    Lê todas as frases da aba ativa e retorna como lista de dicionários
    """
    dados = aba.get_all_records()  # retorna lista de dicts
    frases_ativas = [d for d in dados if d["status"] == "ativa"]
    return frases_ativas

def sortear_frase_atualizada(aba):
    frases = carregar_frases_atualizadas(aba)
    if not frases:
        return None
    
    # Ordena pelo menor 'vezes_usada'
    frases.sort(key=lambda x: x["vezes_usada"])
    menor_uso = frases[0]["vezes_usada"]

    # Filtra só as frases com menor uso
    candidatos = [f for f in frases if f["vezes_usada"] == menor_uso]

    # Sorteia uma
    return random.choice(candidatos)
