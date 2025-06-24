# Projeto de Pipeline de Dados

Projeto final da disciplina Linguagens de Programação para Engenharia de Dados

## Estrutura do Projeto

pipeline/
├── data/                  # (Dados simulados gerados com a biblioteca Faker e salvos com formatos variados.)
│   ├── dados1.csv
│   ├── dados2.parquet
│   ├── dados3.feather
│   ├── extrair.csv          # (Gerado pela etapa de extração)
│   ├── transformar.csv    # (Gerado pela etapa de transformação)
│   └── carregar.csv         # (Gerado pela etapa de carga)
├── logs/
│   └── execucao.log       # (Log da execução das tarefas)
├── src/
│   ├── main.py            # (Ponto de entrada da pipeline)
│   ├── task.py            # (Classe base Task)
│   ├── tasks/
│   │   ├── extrair.py     # Etapa 1: (Extrair)
│   │   ├── transformar.py # Etapa 2: (Tranformar)
│   │   └── carregar.py    # Etapa 3: (Carregar)
│   └── utils/
│       └── logger.py      # Decorator de log
├── teste_logger.py        # Script de teste do logger (só teste)

## Etapas da Pipeline

1. Extração: Faz a leitura de dados de três arquivos em formatos diferentes (csv, parquet, feather) e unifica tudo em extrair.csv.

2. Transformação: Faz a leitura de extrair.csv, gerado na etapa anterior e remove dados nulos e salva o resultado como transformar.csv.

3. Carga: Faz a leitura de transformar.csv, gerado na etapa anterior e gera carregar.csv, para simular a etapa final do processo de Etl.

## Execução

Para rodar a pipeline, entre na pasta pipeline/ e execute:

python -m src.main

## É para saír no terminal:

Executando tarefa: Extrair
Tarefa Extrair finalizada com sucesso.

Executando tarefa: Transformar
Tarefa Transformar finalizada com sucesso.

Executando tarefa: Carregar
Tarefa Carregar finalizada com sucesso.

## Exemplo de log (logs/execucao.log)

[2025-06-22 15:31:21] Extrair: OK - 0.112s
[2025-06-22 15:31:22] Transformar: OK - 0.089s
[2025-06-22 15:31:22] Carregar: OK - 0.072s

## Requisitos

As principais bibliotecas utilizadas são:

- pandas
- pyarrow
