import pandas as pd
from pathlib import Path
from ..task import Task
from ..utils.logger import log_execucao

class Extrair(Task):
    @log_execucao("Extrair")
    def run(self):
        base_path = Path(__file__).resolve().parents[2] / 'data'

        df_csv = pd.read_csv(base_path / "dados1.csv")
        df_parquet = pd.read_parquet(base_path / "dados2.parquet")
        df_feather = pd.read_feather(base_path / "dados3.feather")
        df_total = pd.concat([df_csv, df_parquet, df_feather], ignore_index=True)
        df_total.to_csv(base_path / "extrair.csv", index=False)
