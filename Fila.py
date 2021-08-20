class FilaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class FilaEncadeada:
  def __init__(self):
    self._primeiro = None
    self._tamanho = 0

  @property
  def inicio(self):
    if self.vazia():
      raise FilaException('A fila está vazia')

    return self._primeiro

  def vazia(self):
    return self._tamanho == 0
  
  def tamanho(self):
    return self._tamanho
  
  def inserir(self, dado):
    pontInsert = self._primeiro

    if pontInsert == None:
      self._primeiro = dado

    else:
      while pontInsert.prox != None:
        pontInsert = pontInsert.prox
    
      pontInsert.prox = dado

    self._tamanho += 1 

  def remover(self):
    if self.vazia():
      raise FilaException('A Fila está vazia')

    self._primeiro = self._primeiro.prox
    self._tamanho -= 1 
  
  def __str__(self):
    output = 'Surfistas:\nNome — Quantidade de Títulos\n\n'
    p = self._primeiro

    while p != None:
      output += f'{p.nome} — {p.titulos}\n'
      p = p.prox

      if p != None:
        output += ''
    
    output += ''
    return output

  def mostrarElemento(self):
    pontFind = self._primeiro

    select = (f'Nome: {pontFind.nome}\nTitulos: {pontFind.titulos}\nIdade: {pontFind.idade}\nCPF: {pontFind.cpf}')
    return select

  def imprimir(self):
    print(self.__str__())