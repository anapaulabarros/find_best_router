from Controller.Main import *
from flask import Flask
from flask import render_template
from flask import redirect, request
from flask import url_for



app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/arquivo')
def openFile():
    return render_template('rotas.html', rotas = controller_api.grafo.lista_Arestas)


@app.route('/novo')
def novo():
    return render_template('adicionar.html')

@app.route('/busca')
def busca():
    return render_template('consultarota.html')

@app.route('/criar', methods=['POST',])
def criar():
    origem = request.form['origem']
    destino = request.form['destino']
    custo = request.form['custo']
    controller_api.atualizaGrafo(origem, destino, custo)
    controller_api.arquivo.writeArquivo(origem, destino, custo)
    return redirect(url_for('home'))


@app.route('/caminho', methods=['POST',])
def caminho():
    origem = Vertice(request.form['origem'])
    destino = Vertice(request.form['destino'])

    rota, custo = controller_api.obterRotaDijkstra(origem.getId(), destino.getId())

    return render_template('consultarota.html', rotas = rota, custo = custo)


if __name__ == '__main__':

    args = []

    for param in sys.argv:
        args.append(param)
    nome_ficheiro = args[1]

    controller_api = Main(nome_ficheiro)
    controller_api.tratar_dados_de_entrada()
    controller_api.monta_grafo()

    app.run(host='127.0.0.10', port='5000', debug=True)