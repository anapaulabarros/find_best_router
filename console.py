from Controller.Main import *
from sys import *


def menu():

    return print('''
        /////////  MENU  /////////
        1 - Para listar Rotas 
        2 - Para add nova rota
        3 - Para consultar rota
        0 - Para sair
        //////////////////////////
        ''')

def printRotas(rotas):

    for rota in rotas:
        print('Origem: {}'.format(rota.origem.id))
        print('Destino: {}'.format(rota.destino.id))
        print('Custo: {}'.format(rota.peso))
        print('\n')

def adicionarRota(grafo):
    print('Informe a nova rota no formato: Origem,Destino,Custo')
    origem, destino, custo = input().split(',')
    grafo.atualizaGrafo(origem, destino, custo)
    if grafo.arquivo.writeArquivo(origem, destino, custo):
        print('Rota adiconada com sucesso')
    else:
        print('Ocorreu algum erro ao atualiza o arquivo')

def obterViagem(grafo):
    print('Informe qual a viagem no formato: Origem-Destino: ')
    origem, destino = input().split('-')
    origem = Vertice(origem)
    destino = Vertice(destino)

    rota, custo = grafo.obterRotaDijkstra(origem.getId(), destino.getId())

    print('Rota: {} \n'. format(rota))
    print('Custo: {} \n'. format(custo))

if __name__ == '__main__':

    args = []

    for param in sys.argv:
        args.append(param)
    # nome_ficheiro = args[1]
    nome_ficheiro = 'input-fileCp.csv'
    controller_api = Main(nome_ficheiro)
    controller_api.tratar_dados_de_entrada()
    controller_api.monta_grafo()
    option = 999
    while option != 0:
        menu()
        option = int(input('Informe qual operação deseja realizar: '))

        if option == 1:
            printRotas(controller_api.grafo.lista_Arestas)
        elif option == 2:
            adicionarRota(controller_api)
        elif option == 3:
            obterViagem(controller_api)
        elif option == 0:
            print('Bye')
        else :
            print('Opção Invalida')


