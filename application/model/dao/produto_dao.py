from application.model.entity.produto import Produto
from application import listaProdutos

class ProdutoDAO:

    def __init__(self):
        self._listaProdutos = listaProdutos
    
    def listar_produtos(self):
        return self._listaProdutos
    
    def buscar_por_id(self, id):
        for produto in range(0, len(self._listaProdutos)):
            if self._listaProdutos[produto].get_id() == int(id):
                return self._listaProdutos[produto]
        return None