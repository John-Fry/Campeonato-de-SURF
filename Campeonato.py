from Lista import ListaEncadeada, ListaException
from Fila import FilaEncadeada, FilaException
from Pilha import PilhaEncadeada, PilhaEncadeada

class Campeonato:
  def __init__(self, nome_camp):
    self._nome_camp = str(nome_camp)
    self._surfistasL = ListaEncadeada()
    self._surfistasP = PilhaEncadeada()
    self._surfistasF = FilaEncadeada()

  @property
  def nome_camp(self):
    return self._nome_camp

  @nome_camp.setter
  def nome_camp(self, novo_camp):
    self._nome_camp = novo_camp
  
  def adicionar_surfistasL(self, surfista, posicao):
    self._surfistasL.inserir(surfista, posicao)

  def adicionar_surfistasP(self, surfista):
    self._surfistasP.inserir(surfista)
  
  def adicionar_surfistasF(self, surfista):
    self._surfistasF.inserir(surfista)

  def buscar_surfistaCPF(self, cpf):
    return self._surfistasL.buscarCPF(cpf)
  
  def remover_surfistaL(self, posicao):
    self._surfistasL.remover(posicao)
  
  def remover_surfistaF(self):
    self._surfistasF.remover()
  
  def remover_surfistaP(self):
    self._surfistasP.remover()
  
  def ordenar_surfistasL(self):
    self._surfistasL.ordenar()
  
  def imprimirSurfistasL(self):
    self._surfistasL.imprimir()
  
  def imprimirSurfistasF(self):
    self._surfistasF.imprimir()
  
  def imprimirSurfistasP(self):
    self._surfistasP.imprimir()

  def mostrar_tam_surfistasL(self):
    return self._surfistasL.tamanho()
  
  def mostrar_tam_surfistasP(self):
    return self._surfistasP.tamanho()
  
  def mostrar_tam_surfistasF(self):
    return self._surfistasF.tamanho()
  
  def maiorIdade(self):
    tam = self._surfistasL.tamanho()
    maior = 0

    for i in range(tam):
      surfista = self._surfistasL.buscarPosicao(i)
      if (surfista.idade > maior):
        maior = surfista.idade
        output = (f'Nome: {surfista.nome}\n')

    output += (f'Idade: {maior}')
    
    return output
  
  def menorIdade(self):
    tam = self._surfistasL.tamanho()
    menor = 999

    for i in range(tam):
      surfista = self._surfistasL.buscarPosicao(i)
      if (surfista.idade < menor):
        menor = surfista.idade
        output = (f'Nome: {surfista.nome}\n')

    output += (f'Idade: {menor}')
    
    return output

  def incrementaTitulo(self, cpf):
    tam = self._surfistasL.tamanho()
    for i in range(tam):
      surfista = self._surfistasL.buscarPosicao(i)
      if (surfista.cpf == cpf):
        incrementa = surfista
        incrementa.incrementa_titulo()
        incrementa.prox = surfista.prox
        surfista = incrementa
    
    return surfista
  
  def mostrarElemento(self, posicao):
    return self._surfistasL.mostrarElemento(posicao)