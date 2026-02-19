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
