import csv
from os import write
from flask import Flask, render_template, request
import google.generativeai as genai

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def ola():
    # return '<h1>Olá, mundo!</h1>'
    return render_template('index.html')


@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')


@app.route('/glossario')
def glossario():
    glossario_de_termos = []

    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)

    return render_template('glossario.html', glossario=glossario_de_termos)


@app.route('/novo-termo')
def novo_termo():
    return render_template('novo_termo.html')


@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))


@app.route('/excluir_termo/<int:termo_id>', methods=['POST'])
def excluir_termo(termo_id):
    with open('bd_glossario.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break

    with open('bd_glossario.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(linhas)

    return redirect(url_for('glossario'))


@app.route('/editar_termo/<int:termo_id>', methods=['GET'])
def editar_termo(termo_id):
    with open('bd_glossario.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

    termo = linhas[termo_id][0]
    definicao = linhas[termo_id][1]
    return render_template('editar.html', termo=termo, definicao=definicao, termo_id=termo_id)


@app.route('/atualizar_termo', methods=['POST'])
def atualizar_termo():
    id = request.form['termo_id']
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        linhas = list(reader)

        for i, linha in enumerate(linhas):
            if i == int(id):
                linhas[i] = [termo, definicao]
                print('achei o termo', id)

    with open('bd_glossario.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(linhas)

    return redirect(url_for('glossario'))


genai.configure(api_key="AIzaSyAXrWr_CvUhEZfOJh-Rk5_2La_zKK9ptY0")

# Modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro')


@app.route("/duvidas", methods=["GET", "POST"])
def duvidas():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        if pergunta:
            try:
                resultado = model.generate_content(pergunta)
                resposta = resultado.text
            except Exception as e:
                resposta = f"Erro: {str(e)}"
    return render_template("duvidas.html", resposta=resposta)


app.run()
