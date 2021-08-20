class PilhaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)

class PilhaEncadeada:
  def __init__(self):
    self._topo = None
    self._tamanho = 0

  @property
  def topo(self):
    if self.vazia():
      raise PilhaException('A pilha está vazia')

    return self._topo

  def vazia(self):
    return self._tamanho == 0

  def tamanho(self):
    return self._tamanho

  def inserir(self, dado):
    dado.prox = self._topo
    self._topo = dado
    self._tamanho += 1

  def remover(self):
    if self.vazia():
      raise PilhaException('A pilha está vazia')

    self._topo = self._topo.prox
    self._tamanho -= 1
  
  def mostrarElemento(self):
    pontFind = self._topo

    select = (f'Nome: {pontFind.nome}\nTitulos: {pontFind.titulos}\nIdade: {pontFind.idade}\nCPF: {pontFind.cpf}')
    return select

  def __str__(self):
    output = 'Surfistas:\nNome — Quantidade de Títulos\n\n'
    p = self._topo

    while p != None:
      output += f'{p.nome} — {p.titulos}\n'
      p = p.prox

      if p != None:
        output += ''
    
    output += ''
    return output


  def imprimir(self):
    print(self.__str__())