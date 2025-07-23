import os
from react_command.templates import *
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

def criar_arquivos_componente(nome_componente, com_reducer):
    nome_arquivo_componente = f"{nome_componente}.tsx"
    nome_arquivo_componente_css = f"{nome_componente}.module.css"
    nome_arquivo_componente_types = f"{nome_componente}.types.ts"

    path_arquivo_componente = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente)
    path_arquivo_componente_css = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente_css)
    path_arquivo_componente_types = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente_types)

    conteudo_arquivo_componente = obter_template_arquivo_componente(nome_componente, com_reducer)
    conteudo_arquivo_tipos = obter_template_arquivo_types(nome_componente, com_reducer)
    criar_arquivo(path_arquivo_componente, conteudo_arquivo_componente)
    criar_arquivo(path_arquivo_componente_css, '')
    criar_arquivo(path_arquivo_componente_types, conteudo_arquivo_tipos)

    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente}")
    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente_css}")
    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente_types}")

def criar_arquivos_tela_listagem(*, nome_componente, tabela, titulo, subtitulo):
    nome_arquivo_componente = f"{nome_componente}.tsx"
    nome_arquivo_componente_css = f"{nome_componente}.module.css"
    nome_arquivo_componente_types = f"{nome_componente}.types.ts"

    path_arquivo_componente = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente)
    path_arquivo_componente_css = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente_css)
    path_arquivo_componente_types = obter_path_arquivo_componente(nome_componente, nome_arquivo_componente_types)

    conteudo_arquivo_componente = obter_template_tela_listagem(nome_componente, tabela, titulo, subtitulo)
    conteudo_arquivo_tipos = obter_template_tela_listagem_types(nome_componente, tabela)
    conteudo_arquivo_estilos = obter_template_tela_listagem_estilos()
    criar_arquivo(path_arquivo_componente, conteudo_arquivo_componente)
    criar_arquivo(path_arquivo_componente_css, conteudo_arquivo_estilos)
    criar_arquivo(path_arquivo_componente_types, conteudo_arquivo_tipos)

    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente}")
    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente_css}")
    print(f"[blink bold green][CRIADO][/] {path_arquivo_componente_types}")

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
