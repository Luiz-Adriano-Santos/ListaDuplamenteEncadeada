from caixa import Caixa 

class ListaDuplamenteCadeada:
    def __init__(self):
        self.__primeiro = None  
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    def tamanho(self):
        return self.__tamanho
    
    def inserir_antes_do_atual(self, valor):
        novo = valor
        if self.__cursor is None:
            self.__primeiro = novo
            self.__ultimo = novo
            self.__cursor = novo
        else: