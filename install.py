import os
import subprocess
import sys
import site
import shutil

def run(cmd):
    print(f"[Executando]: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# Path do executável do python no sistema
path_exe_python = sys.executable

# Path do diretório do executável do python no sistema
path_diretorio_exe_python = os.path.dirname(path_exe_python)

# Path do diretório de Scripts do python no sistema
scripts_dir = os.path.join(path_diretorio_exe_python, 'Scripts')

# Path do requirements.txt na pasta atual
requeriments_path = os.path.join(os.getcwd(), "requirements.txt")

try: 
    # 1. Instala em modo editável
    run(f'"{path_exe_python}" -m pip install -e .')

    # 2. Instala os requirements
    if os.path.exists(requeriments_path):
        run(f'"{path_exe_python}" -m pip install -r "{requeriments_path}"')
    else: 
        print("Arquivo requirements.txt não encontrado.")

    # 3. Adiciona o diretório do Python ao PATH via PowerShell
    powershell_cmd = f'[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";{scripts_dir}", "User")'


    
    print(f'\n✅ Finalizado com sucesso.\nPython: {path_exe_python}\nPython DIR adicionado ao PATH: {path_diretorio_exe_python}')

except subprocess.CalledProcessError as e:
    print(f'\n❌ Erro ao executar comandos: {e}')