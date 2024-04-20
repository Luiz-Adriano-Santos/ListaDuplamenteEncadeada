class Caixa:
    def __init__(self,valor):
        self.__valor = valor
        self.__proximo = None
        self.__anterior = None

    def valor(self):
        return self.__valor
    
    def proximo(self):
        return self.__proximo
    
    def anterior(self):
        return self.__anterior