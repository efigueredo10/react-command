from .arquivos import *
from rich import print

def criar_tela(nome_tela, com_reducer: True):
    print(f"\n[blink bold magenta][CRIANDO TELA][/] {nome_tela}\n")
    criar_diretorio_componente(nome_tela)
    criar_diretorio_api(nome_tela)
    criar_diretorio_componentes(nome_tela)
    criar_arquivos_componente(nome_tela)
    criar_arquivo_api(nome_tela);

def criar_componente(nome_componente, com_reducer: True):
    print(f"\n[blink bold magenta][CRIANDO COMPONENTE] {nome_componente}[/]\n")
    criar_diretorio_componente(nome_componente)
    criar_arquivos_componente(nome_componente)