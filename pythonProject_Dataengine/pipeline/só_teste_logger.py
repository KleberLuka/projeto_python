from src.utils.logger import log_execucao

@log_execucao("TesteLogger")
def tarefa_exemplo():
    total = 0
    for i in range(1000000):
        total += i
    return total

if __name__ == "__main__":
    tarefa_exemplo()
