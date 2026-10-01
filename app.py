from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
import os
from datetime import datetime

def carregar_solicitacoes():
solicitacoes = []
if os.path.exists(ARQUIVO):
with open(
ARQUIVO, "r", newline="", encoding="utf-8"
) as arquivo:
leitor = csv.DictReader(arquivo)
solicitacoes.extend(leitor)
return solicitacoes

def salvar_solicitacoes(solicitacoes):
with open(
ARQUIVO, "w", newline="", encoding="utf-8"
) as arquivo:
escritor = csv.DictWriter(
arquivo, fieldnames=CAMPOS
)
escritor.writeheader()
escritor.writerows(solicitacoes)

@app.route("/")
def inicio():
solicitacoes = carregar_solicitacoes()
return render_template(
"index.html",
solicitacoes=solicitacoes
)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
solicitacoes = carregar_solicitacoes()
nova_solicitacao = {
"id": gerar_novo_id(solicitacoes),
"nome": request.form.get( "nome", "" ).strip(),
"tipo_usuario": request.form.get( "tipo_usuario", "" ).strip(),
"sala": request.form.get( "sala", "" ).strip(),
"equipamento": request.form.get( "equipamento", "" ).strip(),
"descricao": request.form.get( "descricao", "" ).strip(),
"data": datetime.now().strftime( "%d/%m/%Y %H:%M" ),
"status": "Pendente"
}
campos_obrigatorios = [
"nome",
