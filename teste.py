from caixa import Caixa
from lista_duplamente_encadeada import ListaDuplamenteEncadeada


lista = ListaDuplamenteEncadeada(10)

# teste de inserção como ultimo

lista.inserir_como_ultimo(Caixa("A"))
lista.inserir_como_ultimo(Caixa("B"))
lista.inserir_como_ultimo(Caixa("C"))

print("Lista após inserção de três elementos:")
lista.exibir_lista()

# teste de inserção como primeiro

lista.inserir_como_primeiro(Caixa("0"))

print("Lista após inserção no início:")
lista.exibir_lista()

# teste de inserção após atual

lista.ir_para_primeiro()
lista.inserir_apos_atual(Caixa("AA"))

print("Lista após inserção após o primeiro elemento:")
lista.exibir_lista()

# teste de inserção antes do atual

lista.inserir_antes_do_atual(Caixa("-1"))

print("Lista após inserção antes do elemento atual:")
lista.exibir_lista()

# teste de exclusão do atual

lista.ir_para_primeiro()
lista.avancar_k_posicoes(3)

lista.excluir_atual()

print("Lista após exclusão do elemento atual (Elemento A):")
lista.exibir_lista()

# teste busca

elemento = Caixa("D")

lista.inserir_apos_atual(elemento)

print("Lista após inserção do elemento D:")
lista.exibir_lista()

lista.buscar(elemento.chave())
elemento_encontrado = lista.acessar_atual()
print("Elemento encontrado na busca:", elemento_encontrado if elemento_encontrado else "Não encontrado")

# teste de posição

posicao = lista.posicao_de(elemento.chave())
print("Posição do elemento D:", posicao)

# teste de cheia e vazia

print("A lista está cheia?", lista.cheia())
print("A lista está vazia?", lista.vazia())
