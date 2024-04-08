from fastapi import APIRouter, HTTPException, UploadFile, File
from mod_produto.Produto import Produto
import db
from mod_produto.ProdutoModel import ProdutoDB
from fastapi import Depends
from security import get_current_active_user

router = APIRouter(dependencies=[Depends(get_current_active_user)])

@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        produtos = session.query(ProdutoDB).all()
        return produtos, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id_produto}", tags=["Produto"])
def get_produto_por_id(id_produto: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id_produto).first()
        if produto is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return produto, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(produto: Produto):
    try:
        session = db.Session()
        novo_produto = ProdutoDB(nome=produto.nome, descricao=produto.descricao, foto=produto.foto, valor_unitario=produto.valor_unitario)
        session.add(novo_produto)
        session.commit()
        return {"id": novo_produto.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id_produto}", tags=["Produto"])
def put_produto(id_produto: int, produto: Produto):
    try:
        session = db.Session()
        produto_existente = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id_produto).first()
        if produto_existente is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        produto_existente.nome = produto.nome
        produto_existente.descricao = produto.descricao
        produto_existente.valor_unitario = produto.valor_unitario
        produto_existente.foto = produto.foto  # Atualizar a foto
        
        session.commit()
        return {"id": produto_existente.id_produto,
                "nome": produto_existente.nome}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id_produto}", tags=["Produto"])
def delete_produto(id_produto: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id_produto).first()
        if produto is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        session.delete(produto)
        session.commit()
        return {"id": id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
