from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

URL = "mysql+mysqlconnector://<user>:<password>@127.0.0.1:3306/prova_abd"
engine = create_engine(url=URL)

Base = declarative_base()

class Pais(Base):
    __tablename__ = "Pais"
    id_pais = Column(Integer, primary_key=True)
    nome_pais = Column(String(150), nullable=False)


class Estado(Base):
    __tablename__ = "Estado"
    id_estado = Column(Integer, primary_key=True, nullable=False)
    nome_estado = Column(String(150), nullable=False)
    id_pais = Column(Integer, ForeignKey("Pais.id_pais"), nullable=False)


class Cidade(Base):
    __tablename__ = "Cidade"
    id_cidade = Column(Integer, primary_key=True, nullable=False)
    nome_cidade = Column(String(150), nullable=False)
    id_estado = Column(Integer, ForeignKey("Estado.id_estado"), nullable=False)


class Endereco(Base):
    __tablename__ = "Endereco"
    id_endereco = Column(Integer, primary_key=True, nullable=False)
    id_cidade = Column(Integer, ForeignKey("Cidade.id_cidade"), nullable=False)
    nome_rua = (Column(String(150), nullable=False))


class Usuario(Base):
    __tablename__ = "Usuario"
    cpf = Column(String(150), primary_key=True, nullable=False)
    nome_usuario = Column(String(150), nullable=False)
    data_login = Column(String(20), nullable=False)
    idade = Column(Integer)
    id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"), nullable=False)


class Venda(Base):
    __tablename__ = "Venda"
    id_venda = Column(Integer, primary_key=True, nullable=False)
    id_vendedor = Column(Integer, ForeignKey("Vendedor.id_vendedor"), nullable=False)
    id_produto = Column(Integer, ForeignKey("Produto.id_produto"), nullable=False)
    data_venda = Column(String(20), nullable=False)


class Vendedor(Base):
    __tablename__ = "Vendedor"
    id_vendedor = Column(Integer, primary_key=True, nullable=False)
    nome_vendedor = Column(String(150), nullable=False)
    idade = Column(Integer, nullable=False)



class Produto(Base):
    __tablename__ = "Produto"
    id_produto = Column(Integer, primary_key=True, nullable=False)
    nome_produto = Column(String(150), nullable=False)
    tipo = Column(String(150), nullable=False)
    quantidade_disponiveis = Column(Integer, nullable=False)


class Compra(Base):
    __tablename__ = "Compra"
    id_compra = Column(Integer, primary_key=True, nullable=False)
    id_usuario = Column(String(150), ForeignKey("Usuario.cpf"), nullable=False)
    id_produto = Column(Integer, ForeignKey("Produto.id_produto"), nullable=False)
    data_compra = Column(String(20), nullable=False)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

with Session.begin() as session:
    pais = Pais(
        id_pais = 1,
        nome_pais = "Brasil"
    )
    session.add(pais)

with Session.begin() as session:
    estado = Estado(
        id_estado = 1,
        nome_estado = "Sao Paulo",
        id_pais = 1
    )
    session.add(estado)    
    