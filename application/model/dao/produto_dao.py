from application.model.entity.produto import Produto
import json

class ProdutoDAO:

    def __init__(self):
        self._listaProdutos = []
    
        with open('C:\\Users\\pedro\\Documents\\Arquivos Pedro\\Arquivos da Faculdade\\Laboratório de Programação de Interface com o Usuário\\Prova P2\\prova-labprogint\\application\\view\\static\\json\\products.json') as product_file:
            product_list = json.load(product_file)
    
        for product in product_list:
            self._listaProdutos.append(Produto(product['id'],product['name'], product['image'], product['description'], product['oldPrice'], product['price'], product['installments']['value'], product['installments']['count']))

    def get_listar_produtos(self):
        return self._listaProdutos