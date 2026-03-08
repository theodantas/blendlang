# nucleo/conexao_planilha.py
import gspread
from google.oauth2.service_account import Credentials

def conectar_planilha():
    escopo = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    credenciais = Credentials.from_service_account_file(
        "credenciais_google.json",
        scopes=escopo
    )

    cliente = gspread.authorize(credenciais)

    planilha = cliente.open("blendlang_frases")
    aba = planilha.sheet1

    return aba

def atualizar_vezes_usada(aba, frase_id):

    celula = aba.find(str(frase_id))

    if not celula:
        return

    linha = celula.row

    # coluna 6 = vezes_usada na sua planilha
    coluna_vezes_usada = 6

    valor_atual = aba.cell(linha, coluna_vezes_usada).value

    if valor_atual is None:
        valor_atual = 0
    else:
        valor_atual = int(valor_atual)

    aba.update_cell(linha, coluna_vezes_usada, valor_atual + 1)