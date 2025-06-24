import pandas as pd
from pathlib import Path
from ..task import Task
from ..utils.logger import log_execucao

class Carregar(Task):
    @log_execucao("Carregar")
    def run(self):
        base_path = Path(__file__).resolve().parents[2] / 'data'

        df = pd.read_csv(base_path / 'transformar.csv')
        df.to_csv(base_path / 'carregar.csv', index=False)
