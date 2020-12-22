from flask import Flask
import os
from application.model.entity.produto import Produto

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

produto1 = Produto(1, "Nome do Produto", "Descrição do produto um pouco maior, com duas linhas ou três que explica melhor do que se trata.", "23,99", "19,99", "2x de R$9,99")
produto2 = Produto(2, "Nome do Produto", "Descrição do produto um pouco maior, com duas linhas ou três que explica melhor do que se trata.", "23,99", "19,99", "2x de R$9,99")
produto3 = Produto(3, "Nome do Produto", "Descrição do produto um pouco maior, com duas linhas ou três que explica melhor do que se trata.", "23,99", "19,99", "2x de R$9,99")
produto4 = Produto(4, "Nome do Produto", "Descrição do produto um pouco maior, com duas linhas ou três que explica melhor do que se trata.", "23,99", "19,99", "2x de R$9,99")

listaProdutos = [produto1, produto2, produto3, produto4]


from application.controller import index_controller
