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
