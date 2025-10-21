from sqlmodel import create_engine, SQLModel, Session

db_name = ''
db_url = f''
engine = create_engine(db_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def db_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()