from react_command.arquivos import *
from rich import print



def criar_componente(nome_componente, com_reducer: True):
    print(f"\n[blink bold magenta][CRIANDO COMPONENTE] {nome_componente}[/]\n")
    criar_diretorio_componente(nome_componente)
    criar_arquivos_componente(nome_componente, com_reducer)
