# Import módulos
from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")

    def hello_word(self):
        print("Hello Word")
