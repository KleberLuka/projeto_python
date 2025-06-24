import logging
import time
from pathlib import Path

# Cria a pasta se não existir
Path("logs").mkdir(parents=True, exist_ok=True)

# Configura o logger
logging.basicConfig(
    filename='logs/execucao.log',
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_execucao(nome_tarefa):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Executando tarefa: {nome_tarefa}")
            inicio = time.time()
            resultado = func(*args, **kwargs)
            duracao = round(time.time() - inicio, 3)
            print(f"Tarefa {nome_tarefa} finalizada com sucesso.\n")
            logging.info(f"{nome_tarefa}: OK - {duracao:.3f}s")
            return resultado
        return wrapper
    return decorator
