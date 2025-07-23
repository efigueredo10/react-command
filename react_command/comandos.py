from argparse import Namespace
from react_command.componentes import *
from enum import Enum
from react_command.telas import *

class Comando(Enum):
    TELA = 'tela'
    COMPONENTE = 'componente'

comandos = {
  Comando.TELA: {
    None: lambda nome_componente, argumentos: criar_tela(nome_componente, argumentos),
    "listagem": lambda nome_componente, argumentos: criar_tela_listagem(nome_componente, argumentos),
  },
  Comando.COMPONENTE: {
    None: 'componente cru',
    "modal": None,
    "modalListaDupla": None
  }
}

def obter_comando(parametros: Namespace):
    comando = parametros.args[0] if len(parametros.args) > 0 else None
    if not comando:
        return
    try:
        comando_enum = Comando(comando)
    except ValueError:
        print(f"Comando inválido: {comando}")
        return
    comando_selecionado = comandos.get(comando_enum)
    subcomando = parametros.args[1] if len(parametros.args) > 1 else None
    return comando_selecionado.get(subcomando)

