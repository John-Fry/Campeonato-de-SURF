class Surfista:
  def __init__(self, nome, titulos, idade, cpf):
    self._nome = str(nome)
    self._titulos = int(titulos)
    self._idade = int(idade)
    self._cpf = int(cpf)
    self._prox = None

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  @property
  def titulos(self):
    return self._titulos

  @titulos.setter
  def titulos(self, novo_titulo):
    self._titulos = novo_titulo

  @property
  def idade(self):
    return self._idade

  @idade.setter
  def idade(self, nova_idade):
    self._idade = nova_idade

  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self, novo_cpf):
    self._cpf = novo_cpf

  @property
  def prox(self):
    return self._prox

  @prox.setter
  def prox(self, novo):
    self._prox = novo

  def incrementa_titulo(self):
    self._titulos += 1