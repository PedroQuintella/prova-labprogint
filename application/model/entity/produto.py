class Produto:

    def __init__(self, id, nome, fotoProduto, descricao, precoNormal, precoPromocional, valorParcela, qtdParcela):
        self._id = id
        self._fotoProduto = fotoProduto
        self._nome = nome
        self._descricao = descricao
        self._precoNormal = precoNormal
        self._precoPromocional = precoPromocional
        self._valorParcela = valorParcela
        self._qtdParcela = qtdParcela
    
    def get_id(self):
        return self._id
    
    def get_fotoProduto(self):
        return self._fotoProduto
    
    def get_nome(self):
        return self._nome
    
    def get_descricao(self):
        return self._descricao
    
    def get_precoNormal(self):
        return self._precoNormal
    
    def get_precoPromocional(self):
        return self._precoPromocional
    
    def get_valorParcela(self):
        return self._valorParcela

    def get_qtdParcela(self):
        return self._qtdParcela

    
    
