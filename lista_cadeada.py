from caixa import Caixa


class ListaDuplamenteCadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    def tamanho(self):
        return self.__tamanho

    def acessar_atual(self):
        if self.__cursor is None:
            return None
        return self.__cursor.valor()

    def inserir_antes_do_atual(self, novo):
        if self.__cursor is None:
            self.__primeiro = novo
            self.__ultimo = novo
            self.__cursor = novo
        else:
            anterior = self.__cursor.anterior()
            if anterior is None:
                self.__primeiro = novo
            else:
                anterior.set_proximo(novo)
            novo.set_proximo(self.__cursor)
            novo.set_anterior(anterior)
            self.__cursor.set_anterior(novo)
        self.__tamanho += 1

    def inserir_apos_atual(self, novo):
        if self.__cursor is None:
            self.__primeiro = novo
            self.__ultimo = novo
            self.__cursor = novo
        else:
            proximo = self.__cursor.proximo()
            if proximo is None:
                self.__ultimo = novo
            else:
                proximo.set_anterior(novo)
            novo.set_anterior(self.__cursor)
            novo.set_proximo(proximo)
            self.__cursor.set_proximo(novo)
        self.__tamanho += 1

    def inserir_como_ultimo(self, novo):
        if self.__cursor is None:
            self.__primeiro = novo
            self.__ultimo = novo
            self.__cursor = novo
        else:
            self.__ultimo.set_proximo(novo)
            novo.set_anterior(self.__ultimo)
            self.__ultimo = novo
        self.__tamanho += 1

    def inserir_como_primeiro(self, novo):
        if self.__cursor is None:
            self.__primeiro = novo
            self.__ultimo = novo
            self.__cursor = novo
        else:
            self.__primeiro.set_anterior(novo)
            novo.set_proximo(self.__primeiro)
            self.__primeiro = novo
        self.__tamanho += 1

    def inserir_na_posicao(self, k, novo):
        if k < 0 or k > self.__tamanho:
            return False
        self.__cursor = self.__primeiro
        for i in range(k):
            self.__cursor = self.__cursor.proximo()
        self.inserir_antes_do_atual(novo)
        return True

    def buscar(self, chave):
        self.__cursor = self.__primeiro
        while self.__cursor is not None:
            if self.__cursor.chave() == chave:
                return True
            self.__cursor = self.__cursor.proximo()
        return False
