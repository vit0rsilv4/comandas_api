from fastapi import APIRouter
from mod_cliente.ClienteModel import ClienteDB
from mod_cliente.Cliente import Cliente
import db


router = APIRouter()
# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    try:
        session = db.Session()
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(cliente: Cliente):
    try:
        session = db.Session()
        novo_cliente = ClienteDB(nome=cliente.nome, cpf=cliente.cpf, telefone=cliente.telefone)
        session.add(novo_cliente)
        session.commit()
        return {"id": novo_cliente.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, cliente: Cliente):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        dados.nome = cliente.nome
        dados.cpf = cliente.cpf
        dados.telefone = cliente.telefone
        session.commit()
        return {"id": dados.id_cliente, 
                "nome": dados.nome}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("cliente/cpf/{cpf}", tags=["Cliente"])
def verifyClientCpf(cpf: str):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.cpf == cpf)

        return dados
    except Exception as e:

        return {"erro", str(e)}, 400
    finally:
        session.close()