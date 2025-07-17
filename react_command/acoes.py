from enum import Enum
from .componentes import *

class Acao(Enum):
    TELA = "tela"
    COMPONENTE = "componente"
    

def obter_acao(args) -> Acao:
    acao = None;
    if args.tela:
        acao = Acao.TELA
    else:
        acao = Acao.COMPONENTE
    return acao;
    

def obter_funcao_acao(acao: Acao):
    acoes = {
        Acao.TELA.value: lambda nome_componente, com_reducer: criar_tela(nome_componente, com_reducer),
        Acao.COMPONENTE.value: lambda nome_componente, com_reducer: criar_componente(nome_componente, com_reducer)
    }
    return acoes[acao.value]