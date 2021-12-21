# api criada utilizando 
# https://replit.com/@Elcimarsilva/MinhaAPI#main.py


import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/')
def homepage():
  return 'Homepage do site'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

app.run(host='0.0.0.0')