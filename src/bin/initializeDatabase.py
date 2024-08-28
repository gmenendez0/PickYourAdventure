import subprocess
import os

SCRIPT1 = "createDatabase.py"
SCRIPT2 = "loadAdventures.py"


def run_script(script_path):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        print(f"Ejecutando {script_path}...")
        subprocess.run(["python", script_path], check=True)
        print(f"{script_path} ejecutado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {script_path}: {e}")


if __name__ == "__main__":
    run_script(SCRIPT1)
    run_script(SCRIPT2)
