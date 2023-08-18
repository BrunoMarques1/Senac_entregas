from abc import ABC, abstractmethod
class Computador(ABC):
    def __init__(self, modelo=None, cor=None, preco=None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.preco}"        

    @abstractmethod
    def cadastrar(self):
        pass

