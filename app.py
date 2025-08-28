import subprocess

def run_server():
    command = ["uvicorn", "src.api.backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    print(f"Запускаю команду: {' '.join(command)}")
    subprocess.run(command, text=True, check=True, capture_output=False)

if __name__ == "__main__":
    run_server()