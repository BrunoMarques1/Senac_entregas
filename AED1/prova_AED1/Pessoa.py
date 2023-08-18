from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self._telefone = telefone
    
    @abstractmethod
    def marcarPresenca(self):
        pass
    
    @abstractmethod
    def matricular():
        pass