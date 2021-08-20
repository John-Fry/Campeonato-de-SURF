from Surfista import Surfista

class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class ListaEncadeada:
  def __init__(self):
    self._head = None
    self._tamanho = 0
  
  @property
  def inicio(self):
    return self._head

  def vazia(self):
    return self._tamanho == 0
  
  def tamanho(self):
    if self.vazia():
      raise ListaException('A lista está vazia')
    else:
      return self._tamanho
  
  def inserir(self, dado, posicao):
    pontInsert = self._head
    cont = 0
    self._tamanho += 1

    if (posicao == 0):
      dado.prox = self._head
      self._head = dado
      return ''

    while ((pontInsert != None) and (cont < posicao - 1)):
      pontInsert = pontInsert.prox
      cont += 1

    dado.prox = pontInsert.prox
    pontInsert.prox = dado
      
  def remover(self, posicao):
    if self.vazia():
      raise ListaException('A lista está vazia')
    else:
      pontLixeiro = self._head
      cont = 0
      pontDelete = None
      
      if (posicao == 0):
        self._head = self._head.prox
        return ''

      else:
        while ((pontLixeiro.prox != None) and (cont < posicao)):
          pontDelete = pontLixeiro
          pontLixeiro = pontLixeiro.prox
          cont += 1
        
        pontDelete.prox = pontLixeiro.prox
      
      self._tamanho -= 1
  
  def mostrarElemento(self, posicao):
    pontFind = self._head
    cont = 0
    select = None

    while ((pontFind.prox != None) and (cont < posicao)):
      pontFind = pontFind.prox
      cont += 1
    
    select = (f'Nome: {pontFind.nome}\nTitulos: {pontFind.titulos}')

    return select
  
  def buscarCPF(self, cpf):
    pontDetetive = self._head
    search = None

    while (pontDetetive != None):
      pontDetetive = pontDetetive
      if (pontDetetive.cpf == cpf):
        search = (f'Nome: {pontDetetive.nome}\nIdade: {pontDetetive.idade}\nCPF: {pontDetetive.cpf}\nTitulos: {pontDetetive.titulos}')
    
      pontDetetive = pontDetetive.prox

    return search
  
  def buscarPosicao(self, posicao):
    pontDetetive = self._head
    search = None
    cont = 0

    while ((cont < posicao) and (pontDetetive.prox != None)):
      pontDetetive = pontDetetive.prox
      cont += 1
    
    search = pontDetetive
    
    return search
  
  def ordenar(self):
    tail = None
    while self._head != tail:
      r = p = self._head
      while p.prox != tail:
        q = p.prox
        if p.nome > q.nome:
          p.prox = q.prox
          q.prox = p
          if p != self._head:
            r.prox = q
          else:
            self._head = q
          p, q = q, p
        r = p
        p = p.prox
      tail = p
    
    output = 'Lista: ['
    z = self._head

    while z != None:
      output += f'[{z.nome}, {z.titulos}, {z.idade}, {z.cpf}]'
      z = z.prox

      if z != None:
        output += ', '
    
    output += ']'
    return output
    
  def __str__(self):
    output = '\nSurfistas:\n'
    p = self._head

    while p != None:
      output += f'\n{p.nome} — {p.titulos}\n'
      p = p.prox

      if p != None:
        output += ''
    
    output += ''
    return output

  def imprimir(self):
    print(self.__str__())
  