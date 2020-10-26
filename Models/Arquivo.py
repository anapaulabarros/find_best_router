# -*- coding: utf-8 -*-

import csv
from Models.Grafo import *

class Arquivo(object):

	#Método construtor da classe
	def __init__(self, arquivo_entrada = None):
		self.arquivo_entrada = arquivo_entrada
		self.grafo = {}
		self.dadosEntrada = []


	def abrir_arquivo(self, arquivo, modo_abertura):
		return open(arquivo, modo_abertura)

	#Função ler os dados do arquivo de entrada grava em uma lista de dados e retorna está lista de dados
	def ler_arquivo(self):

		lista_dados = []

		with self.abrir_arquivo(self.arquivo_entrada, "r") as ficheiro:
			reader = csv.reader(ficheiro)
			try:
				for linha in reader:
					lista_dados.append(linha)
			except csv.Error as e:
				sys.exit('ficheiro %s, linha %d: %s' % (self.arquivo_entrada, reader.line_num, e))

		ficheiro.close()
		self.dadosEntrada = lista_dados

	#função que ler o arquivo de entrada
	def ler_entrada(self):
		self.ler_arquivo()


	def writeArquivo(self, origem, destino, custo):
		try:
			novarota = origem + ',' + destino + ',' + custo
			with open(self.arquivo_entrada, 'a+') as ficheiro:
				ficheiro.write('\n')
				ficheiro.write(novarota)
				ficheiro.close()

			return True
		except:
			return False