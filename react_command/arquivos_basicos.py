import os
from react_command.templates.api.templates_api import *
from rich import print

def criar_diretorio_componente(nome_componente):
    path = obter_path_dir_componente(nome_componente)
    criar_dir(path)
    print(f"[blink bold green][CRIADO][/] {path}")

def criar_diretorio_api(nome_componente):
    path = obter_path_dir_api(nome_componente)
    criar_dir(path)
    print(f"[blink bold green][CRIADO][/] {path}")

def criar_diretorio_componentes(nome_componente):
    pathDirBase = obter_path_dir_componente(nome_componente)
    path = os.path.join(pathDirBase, 'components')
    criar_dir(path)
    print(f"[blink bold green][CRIADO][/] {path}")

def criar_arquivo_api(nome_componente):
    nome_arquivo_api = f"{nome_componente}.api.ts"
    path = obter_path_arquivo_api(nome_componente, nome_arquivo_api)
    conteudo_arquivo_api = obter_template_arquivo_api(nome_componente)
    criar_arquivo(path, conteudo_arquivo_api)
    print(f"[blink bold green][CRIADO][/] {path}")

def criar_dir(path):
    os.makedirs(path, exist_ok=True)

def criar_arquivo(path, conteudoInicial):
    with open(path, "w", encoding="utf-8") as f:
        f.write(conteudoInicial)

def obter_path_dir_componente(nome_componente):
    return  os.path.join(os.getcwd(), nome_componente)

def obter_path_dir_api(nome_componente):
    pathDirBase = obter_path_dir_componente(nome_componente)
    return os.path.join(pathDirBase, 'api')

def obter_path_arquivo_componente(nome_componente, nome_arquivo):
    pathDirBase = obter_path_dir_componente(nome_componente)
    return os.path.join(pathDirBase, nome_arquivo)

def obter_path_arquivo_api(nome_componente, nome_arquivo):
    pathDirBase = obter_path_dir_api(nome_componente)
    return os.path.join(pathDirBase, nome_arquivo)
