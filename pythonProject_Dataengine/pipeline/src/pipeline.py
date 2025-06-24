class Pipeline:
    def __init__(self, tarefas):
        self.tarefas = tarefas

    def run(self):
        for tarefa in self.tarefas:
            tarefa.run()