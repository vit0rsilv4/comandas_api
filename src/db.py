from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

engine = create_engine(STR_DATABASE, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

def criaTabelas():
    Base.metadata.create_all(engine)


