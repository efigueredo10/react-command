from react_command.comandos import obter_comando
import os
import argparse
from rich.prompt import Prompt

def main():
    limpar_terminal()
    argumentos = obter_argumentos()
    comando = obter_comando(argumentos)
    nome_componente = Prompt.ask(f"[blink bold green][NOME][/]")
    comando(nome_componente, argumentos)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_argumentos():
    parser = argparse.ArgumentParser(description="PARÂMETROS")
    parser.add_argument("args", nargs="+")
    parser.add_argument("--reducer", help="Com Reducer", action='store_true')
    return parser.parse_args()

if __name__ == "__main__":
    main()
