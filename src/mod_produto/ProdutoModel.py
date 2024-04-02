import db
from sqlalchemy import Column, Integer, String, Float, LargeBinary

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    foto = Column(LargeBinary, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    
    def __init__(self, nome, descricao, foto, valor_unitario, id_produto=None):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario