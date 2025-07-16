from .arquivos import *
import os

def main():
    limpar_terminal()
    nome_componente = input("[Nome do componente] => ")
    criar_diretorio_componente(nome_componente)
    criar_diretorio_api(nome_componente)
    criar_diretorio_componentes(nome_componente)
    criar_arquivos_componente(nome_componente)
    criar_arquivo_api(nome_componente)
    
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')