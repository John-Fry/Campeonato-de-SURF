from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  camp1 = Campeonato('WSL')

  s1L = Surfista('Pedro', 1, 25, 421621)
  s2L = Surfista('Joao', 3, 20, 246115)
  s3L = Surfista('John', 2, 21, 1246242)
  s4L = Surfista('Marcos', 2, 19, 1624811)

  camp1.adicionar_surfistasL(s1L, 0)
  camp1.adicionar_surfistasL(s2L, 1)
  camp1.adicionar_surfistasL(s3L, 2)
  camp1.adicionar_surfistasL(s4L, 3)

  s1F = Surfista('Carlos', 3, 22, 236115)
  s2F = Surfista('Artur', 1, 26, 246134)
  s3F = Surfista('Alan', 3, 19, 316241)
  s4F = Surfista('Joel', 2, 18, 624513)

  camp1.adicionar_surfistasF(s1F)
  camp1.adicionar_surfistasF(s2F)
  camp1.adicionar_surfistasF(s3F)
  camp1.adicionar_surfistasF(s4F)

  s1P = Surfista('Nathan', 2, 21, 246812)
  s2P = Surfista('Paulo', 1, 23, 624912)
  s3P = Surfista('Elliot', 3, 27, 126431)
  s4P = Surfista('Jim', 4, 25, 421983)

  camp1.adicionar_surfistasP(s1P)
  camp1.adicionar_surfistasP(s2P)
  camp1.adicionar_surfistasP(s3P)
  camp1.adicionar_surfistasP(s4P)

  #Menu

  def imprimeMenu():
    print(f'''
                        ALOHA!

        |  [1]    Cadastrar Novo Surfista     |
        |  [2]     Acrescentar Título         |
        |  [3]    Buscar Surfista por CPF     |
        |  [4]   Exibir Maior e Menor Idade   |
        |  [5]   Ordernar Surfistas Por Nome  |
        |  [6]   Exibir Surfistas Cadastrados |
        |  [7] Mostrar Quantidade de Surfitas |
        |  [8]       Remover um Surfista      |
        |  [9]             SAIR               |\n''')

  imprimeMenu()
  interacao = int(input('Digite qual opção você deseja acessar: '))

  while True:
    if (interacao == 1):
      nomeRecebe = input('\nDigite o nome do Surfista: ').title()
      titulosRecebe = int(input('Número de Titulos do Surfista: '))
      idadeRecebe = int(input('Idade do Surfista: '))
      cpfRecebe = int(input('CPF do Surfista: '))
      print(f'\nColoque uma posição >= 0 e posição < {camp1.mostrar_tam_surfistasL()}\n')
      posicaoOcup = int(input('Que posição pretende ocupar na lista: '))
      varSurf = Surfista(nomeRecebe, titulosRecebe, idadeRecebe, cpfRecebe)
      camp1.adicionar_surfistasL(varSurf, posicaoOcup)
      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 2):
      incrementa = int(input('\nDeseja incrementar mais um titulo(1-SIM ou 2-NÃO)? '))
      if (incrementa == 1):
        cpfVerify = int(input('\nDigite o CPF do Surfista: '))
        camp1.incrementaTitulo(cpfVerify)
        print('\nTítulo incrementado com Sucesso!\n')
      acessarMenu = int(input('Deseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 3):
      buscaCPF = int(input('\nDigite o CPF do Surfista que deseja buscar: '))
      print()
      print(camp1.buscar_surfistaCPF(buscaCPF))

      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 4):
      print('\nSurfista menor idade')
      print(camp1.menorIdade())
      print()
      print('\nSurfista maior idade')
      print(camp1.maiorIdade())

      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 5):
      camp1.ordenar_surfistasL()
      print('\nSurfistas Ordenados com Sucesso!\n')
      acessarMenu = int(input('Deseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 6):
      camp1.imprimirSurfistasL()

      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 7):
      print(f'\nQuantidade de surfistas cadastrados: {camp1.mostrar_tam_surfistasL()}')

      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      
    elif (interacao == 8):
      remove = int(input('Digite a posição do Surfista que deseja Remover: '))
      print(camp1.mostrarElemento(remove))
      validacao = input(f'Deseja remover o Surfista da posição {remove} S/N? ').upper()
      if validacao == 'S':
        camp1.remover_surfistaL(remove)
        print('\nSurfista foi removido com Sucesso!')
      else:
        remove = int(input('Digite a posição do Surfista que deseja Remover: '))
        print(camp1.mostrarElemento(remove))
        validacao = input(f'Deseja remover o Surfista da posição {remove} S/N? ').upper()

      acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

      if(acessarMenu == 1):
        imprimeMenu()
        interacao = int(input('\nDigite qual opção você deseja acessar: '))
      else:
        interacao = int(input('\nDigite qual opção você deseja acessar: '))

    else:
      break