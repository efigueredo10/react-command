from react_command.arquivos_basicos import *
from rich.prompt import Prompt
from react_command.arquivos.tela_listagem.arquivos_tela_listagem import *
from react_command.arquivos.componente.arquivo_componente import *

def criar_tela(nome_tela, com_reducer: True):
    print(f"\n[blink bold magenta][CRIANDO TELA][/] {nome_tela}\n")
    criar_diretorio_componente(nome_tela)
    criar_diretorio_api(nome_tela)
    criar_diretorio_componentes(nome_tela)
    criar_arquivos_componente(nome_tela, com_reducer)
    criar_arquivo_api(nome_tela);

def criar_tela_listagem(nome_tela, com_reducer: True):
    tabela = Prompt.ask(f"[blink bold green][TABELA][/]")
    titulo = Prompt.ask(f"[blink bold green][TITULO][/]")
    subtitulo = Prompt.ask(f"[blink bold green][SUBTITULO][/]")
    print(f"\n[blink bold magenta][CRIANDO TELA][/] {nome_tela}")
    print(f"\n[blink bold magenta][CRIANDO TABELA][/] {tabela}\n")
    criar_diretorio_componente(nome_tela)
    criar_diretorio_api(nome_tela)
    criar_diretorio_componentes(nome_tela)
    criar_arquivos_tela_listagem(nome_componente=nome_tela, tabela=tabela, titulo=titulo, subtitulo=subtitulo)
    criar_arquivo_api(nome_tela);
