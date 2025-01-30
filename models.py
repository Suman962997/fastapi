from sqlalchemy import Column,Integer,String,Float
from database import Base
# from sqlalchemy.ext.declarative import declarative_base

# Base=declarative_base()

class Employee_class(Base):
    
    __tablename__="roletb"

    id= Column(Integer,primary_key=True)
    register_number=Column(Integer)
    name= Column(String(50))
    department= Column(String(50))
    salary=Column(Float)




# {
#     "secret_key": "admin123",
#     "employee": {
#         "id": 7,
#         "register_number":50365,
#         "name": "raj",
#         "department": "Python developer",
#         "salary": 60000.10
#     }
# }

