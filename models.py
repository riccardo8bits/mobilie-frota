from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuração Base do SQLAlchemy
Base = declarative_base()
# Mudei o nome do banco para frota.sqlite3
engine = create_engine('sqlite:///frota.sqlite3', echo=False)
SessionLocal = sessionmaker(bind=engine)


class Viatura(Base):
    __tablename__ = 'viaturas'

    # Campos simples para teste
    id = Column(Integer, primary_key=True, autoincrement=True)
    prefixo = Column(String, nullable=False) # Ex: VTR-01
    modelo = Column(String, nullable=False)  # Ex: Hilux
    placa = Column(String, nullable=False)   # Ex: ABC-1234




# Função auxiliar para criar as tabelas no arquivo frota.sqlite3 caso não existam
def inicializar_banco():
    Base.metadata.create_all(engine)


inicializar_banco()

def get_todas_viaturas():
    session = SessionLocal()
    # Puxa todas as viaturas do banco
    viaturas = session.query(Viatura).all()
    session.close()
    return viaturas