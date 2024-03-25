from fastapi import APIRouter
from mod_produto.Produto import Produto

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
def get_produtos():
    return {"get todos os produtos"}, 200

@router.get("/produto/{id_produto}", tags=["Produto"], response_model=Produto)
def get_produto_por_id(id_produto: int):
    return {"nome": "teste", "foto": "teste", "valor_unitario": 10.0}, 200

@router.post("/produto/", tags=["Produto"], response_model=Produto)
def post_produto(produto: Produto):
    return produto, 201

@router.put("/produto/{id_produto}", tags=["Produto"], response_model=Produto)
def put_produto(id_produto: int, produto: Produto):
    produto.id_produto = id_produto
    return produto, 200

@router.delete("/produto/{id_produto}", tags=["Produto"])
def delete_produto(id_produto: int):
    return {"msg": "Produto deletado"}, 200