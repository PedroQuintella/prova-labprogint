class Produto:

    def __init__(self, id, nome, descricao, precoPadrao, precoPromocional, parcelamento):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._precoPadrao = precoPadrao
        self._precoPromocional = precoPromocional
        self._parcelamento = parcelamento
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_descricao(self):
        return self._descricao
    
    def get_precoPadrao(self):
        return self._precoPadrao
    
    def get_precoPromocional(self):
        return self._precoPromocional
    
    def get_parcelamento(self):
        return self._parcelamento
    
