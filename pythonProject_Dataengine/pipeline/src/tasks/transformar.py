import pandas as pd
from pathlib import Path
from ..task import Task
from ..utils.logger import log_execucao

class Transformar(Task):
    @log_execucao("Transformar")
    def run(self):
        base_path = Path(__file__).resolve().parents[2] / 'data'
        df = pd.read_csv(base_path / 'extrair.csv')
        df = df.dropna() #->remover linhas vazias
        df.to_csv(base_path / 'transformar.csv', index=False)

