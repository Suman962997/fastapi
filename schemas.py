from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    register_number:int
    name: str
    department: str
    salary: float



class AdminRequest(BaseModel):
    secret_key: str
    employee: Employee = None
