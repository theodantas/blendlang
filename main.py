# main.py
from nucleo.conexao_planilha import conectar_planilha
from nucleo.carregar_frases import sortear_frase_atualizada
from nucleo.mistura import misturar_frase_com_dic

def main():
    # Conecta à planilha
    aba = conectar_planilha()
    
    # Sorteia frase
    frase_info = sortear_frase_atualizada(aba)
    if not frase_info:
        print("Nenhuma frase ativa encontrada!")
        return

    frase_pt = frase_info["texto_pt"]
    linha = frase_info["id"] + 1  # ajusta se a planilha tiver cabeçalho

    # Mistura PT + EN usando dicionário offline
    frase_mista = misturar_frase_com_dic(frase_pt, porcentagem_ingles=50)

    # Atualiza contador 'vezes_usada'
    coluna_vezes_usada = 6  # ajuste conforme sua planilha
    nova_vezes_usada = int(frase_info["vezes_usada"]) + 1
    aba.update_cell(linha, coluna_vezes_usada, nova_vezes_usada)

    # Mostra no terminal
    print("Frase escolhida (PT):", frase_pt)
    print("Frase mista PT + EN:", frase_mista)
    print("Atualizado 'vezes_usada' para:", nova_vezes_usada)

if __name__ == "__main__":
    main()
