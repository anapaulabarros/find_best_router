# -*- coding: utf-8 -*-
# pacotes nativos
import sys
import os
import time

from Models.Grafo import *
from Models.Arquivo import *


class Main(object):

    def __init__(self, arquivo_entrada=None):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo = Arquivo(self.arquivo_entrada)
        self.grafo = Grafo()

    def validar_arquivo(self):

        try:
            # Abro os aqruivos para garantir que não estão corrompidos
            e = open(self.arquivo_entrada, "r")
            # verifica se existe conteudo no arquivo de entrada
            if len(e.readline()) == 0:
                raise IOError

        # tratando os erros
        except IOError:
            # os.system("cls")
            print("\nArquivos de entradas invalidos ou corrompidos")
            sys.exit(0)

    def monta_grafo(self):
        try:
            for arquivo in self.arquivo.dadosEntrada:
                for i in range(0, 2):
                    vertice = Vertice(arquivo[i])
                    self.adicionaVerticeAoGrafo(vertice)
                self.adicionarArestaAoGrafo(arquivo)
        except:
            sys.exit('Erro ao construir Grafo')

    # chama o metodo que ler os dados do arquivo de entrada
    def tratar_dados_de_entrada(self):
        return self.arquivo.ler_entrada()

    def adicionaVerticeAoGrafo(self, vertice):
        exists = self.grafo.busca_Vertice(vertice.getId())
        if (exists):
            return False
        else:
            self.grafo.novo_Vertice(vertice.getId())

    def adicionarArestaAoGrafo(self, linhacsv):
        v1 = Vertice(linhacsv[0])
        v2 = Vertice(linhacsv[1])

        arestajaexiste = self.grafo.busca_Aresta(v1, v2)

        if arestajaexiste is None:
            self.grafo.nova_Aresta(v1.getId(), v2.getId(), int(linhacsv[2]))
        else:
            print("já existe")

    def adicionarArestaAoGrafoII(self, origem, destino, custo):
        arestajaexiste = self.grafo.busca_Aresta(origem, destino )

        if arestajaexiste is None:
            self.grafo.nova_Aresta(origem.getId(), destino.getId(), int(custo))
        else:
            print("já existe")

    def atualizaGrafo(self, origem, destino, custo):

        v1 = Vertice(origem)
        self.adicionaVerticeAoGrafo(v1)

        v2 = Vertice(destino)
        self.adicionaVerticeAoGrafo(v2)

        self.adicionarArestaAoGrafoII(v1, v2, custo)

    def obtemRotaProfunda(self, origem, destino):
        rota = []
        self.grafo.Depth_first_search()
        rota = self.grafo.imprime_Grafo_com_Destino(origem, destino)
        if not rota:
            return None
        rota.reverse()
        return rota

    def obtemRotaLargura(self, origem, destino):
        rota = []
        self.grafo.Breadth_first_search(origem)
        rota = self.grafo.imprime_Grafo_com_Destino(origem, destino)
        if not rota:
            return None
        rota.reverse()
        return rota

    def obterRotaDijkstra(self, origem, destino):
        resposta = self.grafo.Dijkstra(origem)
        rota, custo = self.grafo.imprimirRotaDijsktra(resposta, destino)

        return rota, custo

    def obtemCustoRota(self, origem, destino):
        resposta = self.grafo.Dijkstra(origem.getId())
        custo = 0
        for ele in resposta:
            if ele.id == destino.getId():
                custo = ele.estimativa

        return custo
