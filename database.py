from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base

Base=declarative_base()
engine=create_engine("mysql+pymysql://root:password@localhost:3306/adrole")


Session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
def get_db():
    db=Session()
    try:
        yield db
    finally:
         db.close

