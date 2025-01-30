from fastapi import FastAPI, HTTPException, Depends,APIRouter
from typing import List
from schemas import Employee,AdminRequest
import models
from sqlalchemy.orm import Session
import database


router=APIRouter()
# Simulated secret keys
VALID_ADMIN_SECRET = "admin123"

# Employee model

# Database simulation (in-memory storage)
employee_db = []

# Request model for admin portal authentication

# Function to validate admin access
def verify_admin(secret_key: str):
    if secret_key != VALID_ADMIN_SECRET:
        raise HTTPException(status_code=403, detail="Invalid admin secret key")

# Store employee details (POST)
@router.post("/postemp")
async def add_employee(request: AdminRequest,db:Session=Depends(database.get_db)):
    verify_admin(request.secret_key)
    print("verified")

    emp=request.employee
    user_db=models.Employee_class(id=emp.id,
                register_number=emp.register_number,
                name=emp.name,
                department=emp.department,
                salary=emp.salary)
    
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


# View all employee records (GET)
@router.get("/getall/{secret}")
async def get_all_employees(secret: str,db:Session=Depends(database.get_db)):
    verify_admin(secret)
    print("verified 48")
    all_records = db.query(models.Employee_class).all()

    return all_records


@router.get("/get/{secret}/{intid}")
async def get_employee(secret: str,intid:int,db:Session=Depends(database.get_db)):
    verify_admin(secret)
    intidemp=db.query(models.Employee_class).filter(models.Employee_class.id==intid).first()

    if intidemp is None:
        raise HTTPException(status_code=1000,detail="Employee not found!")
    return intidemp


@router.put('/update/{secret}/{intid}')
async def update_def(secret:str,intid: int, pre:AdminRequest, db: Session = Depends(database.get_db)):
    print("entry")
    verify_admin(secret)
    print("verified 70")
    db_user = db.query(models.Employee_class).filter(models.Employee_class.id == intid).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    data=pre.employee
    db_user.id = data.id
    db_user.register_number = data.register_number
    db_user.name = data.name
    db_user.department =data.department
    db_user.salary = data.salary
    db.commit()
    db.refresh(db_user)
    return db_user#db_user


@router.delete('/delete/{secret}/{intid}')#, response_model=dict)
async def delete_def(secret:str,intid: int, db: Session = Depends(database.get_db)):
    verify_admin(secret)
    print("verified 70")
    db_user = db.query(models.Employee_class).filter(models.Employee_class.id == intid).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "Employee deleted successfully"}



