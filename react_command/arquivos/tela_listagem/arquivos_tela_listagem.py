from react_command.arquivos_basicos import obter_path_arquivo_componente, criar_arquivo
from react_command.templates.tela_listagem.template_tela_listagem import *

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