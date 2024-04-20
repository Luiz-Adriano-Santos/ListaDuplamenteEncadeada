class Caixa:
    def __init__(self, valor):
        self.__chave = id(self)
        self.__valor = valor
        self.__proximo = None
        self.__anterior = None

    def chave(self):
        return self.__chave

    def valor(self):
        return self.__valor

    def proximo(self):
        return self.__proximo

    def anterior(self):
        return self.__anterior

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def set_anterior(self, anterior):
        self.__anterior = anterior
