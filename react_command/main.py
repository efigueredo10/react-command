from react_command.acoes import obter_acao, obter_funcao_acao
import os
import argparse
from rich.prompt import Prompt

def main():
    limpar_terminal()
    argumentos = obter_argumentos()
    acao = obter_acao(argumentos)
    nome_componente = Prompt.ask(f"[blink bold green][NOME {acao.value.upper()}][/]")
    callback_acao = obter_funcao_acao(acao);
    callback_acao(nome_componente, argumentos.reducer)
   
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def obter_argumentos():
    parser = argparse.ArgumentParser(description="Meu comando que aceita parâmetros")
    parser.add_argument("-t", "--tela", help="É tela", action='store_true')
    parser.add_argument("-r", "--reducer", help="Com Reducer", action='store_true')
    return parser.parse_args()

if __name__ == "__main__":
    main()