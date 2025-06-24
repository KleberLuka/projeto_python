from .tasks.extrair import Extrair
from .tasks.transformar import Transformar
from .tasks.carregar import Carregar

def main():
    extrair = Extrair()
    extrair.run()

    transformar = Transformar()
    transformar.run()

    carregar = Carregar()
    carregar.run()

if __name__ == "__main__":
    main()



