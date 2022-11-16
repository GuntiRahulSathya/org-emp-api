from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Utility.database import SessionLocal
from Utility import crud, schemas

org_emp_api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
]

org_emp_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@org_emp_api.get("/")
async def root():
    return {"message": "Hello World"}




@org_emp_api.get("/departments")
async def departments(only_count: bool = False, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_department_count(db)
    return crud.get_departments(db, skip, limit)

@org_emp_api.post("/departments")
async def create_department(dept_data: schemas.DepartmentCreate, department_number: str = None, db: Session = Depends(get_db)):
    return crud.create_department(db, department_number, dept_data)

@org_emp_api.get("/departments/{department_number}")
async def get_department(department_number: str = None, db: Session = Depends(get_db)):
    return crud.get_department(db, department_number)

@org_emp_api.put("/departments/{department_number}")
async def update_department(dept_data: schemas.DepartmentCreate, department_number: str = None, db: Session = Depends(get_db)):
    return crud.update_department(db, department_number, dept_data)

@org_emp_api.delete("/departments/{department_number}")
async def delete_department(department_number: str = None, db: Session = Depends(get_db)):
    return crud.delete_department(db, department_number)



@org_emp_api.get("/employees")
async def get_employees(only_count: bool = False, employee_id: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_employee_count(db)
    elif employee_id:
        return crud.get_filtered_employees(db, employee_id, skip, limit)
    return crud.get_employees(db, skip, limit)

@org_emp_api.post("/employees")
async def create_employee(emp_data: schemas.EmployeeBase = None, db: Session = Depends(get_db)):
    db_data = crud.get_employee_ssn(db, emp_data.ssn)
    if not db_data:
        return crud.create_employee(db, emp_data)
    else:
        raise HTTPException(status_code=404, detail="SSN is part of another employee")

@org_emp_api.get("/employees/fulltime")
async def fulll_timeemployees(only_count: bool = False, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_full_time_employee_count(db)
    return crud.get_fulltime_employees(db)

@org_emp_api.get("/employees/contract")
async def contract_employees(only_count: bool = False, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_contract_employee_count(db)
    return crud.get_contract_employees(db)

@org_emp_api.get("/employees/{employee_id}")
async def get_employee(employee_id: str = None, db: Session = Depends(get_db)):
    out_data = crud.get_employee(db, employee_id)
    if not out_data:
        raise HTTPException(status_code=404, detail="No Employee Present with provided employee_id")
    return crud.get_employee(db, employee_id)

@org_emp_api.put("/employees/{employee_id}")
async def update_employee(employee_id: str, emp_data: schemas.EmployeeBase = None, db: Session = Depends(get_db)):
    print(emp_data)
    db_data = crud.get_employee(db, employee_id)
    if not db_data.employee_id == employee_id:
        raise HTTPException(status_code=404, detail="Employee ID not found")
    return crud.update_employee(db, db_data, emp_data)

@org_emp_api.delete("/employees/{employee_id}")
async def delete_employee(employee_id: str = None, db: Session = Depends(get_db)):
    db_data = crud.get_employee(db, employee_id)
    if not db_data.employee_id == employee_id:
        raise HTTPException(status_code=404, detail="Employee ID not found")
    return crud.delete_employee(db, db_data)




@org_emp_api.get("/employees/{employee_id}/dependents")
async def get_dependents(employee_id: str = None, only_count: bool = False, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_dependent_count(db)
    elif not only_count and employee_id:
        return crud.get_employee_dependents(db, employee_id, skip, limit)

@org_emp_api.post("/employees/{employee_id}/dependents")
async def create_dependents(employee_id: str = None, dependent_data: schemas.DependentCreate = None, db: Session = Depends(get_db)):
    print(employee_id, dependent_data)
    db_data = crud.get_employee(db, employee_id)
    print(db_data.__dict__)
    if db_data:
        return crud.create_employee_dependent(db, dependent_data)
    else:
        raise HTTPException(status_code=404, detail="Employee ID doesn't exist")

@org_emp_api.get("/employees/{employee_id}/dependents/{dependent_id}")
async def get_dependent(employee_id: str = None, dependent_id: str = None, db: Session = Depends(get_db)):
    return crud.get_employee_dependent(db, employee_id, dependent_id)

@org_emp_api.put("/employees/{employee_id}/dependents/{dependent_id}")
async def update_dependents(employee_id: str = None, dependent_id: str = None, db: Session = Depends(get_db)):
    db_data = crud.get_employee_dependent(db, employee_id, dependent_id)
    if not db_data:
        raise HTTPException(status_code=404, detail="Employee ID and dependent_id combination is not found")
    else:
        return crud.update_employee_dependent(db, employee_id, dependent_id)

@org_emp_api.delete("/employees/{employee_id}/dependents/{dependent_id}")
async def delete_dependents(employee_id: str = None, dependent_id: str = None, db: Session = Depends(get_db)):
    db_data = crud.get_employee_dependent(db, employee_id, dependent_id)
    if not db_data:
        raise HTTPException(status_code=404, detail="Employee ID and dependent_id combination is not found")
    return crud.delete_employee_dependent(db, db_data)











@org_emp_api.get("/dependents")
async def dependents(only_count: bool = False, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_dependent_count(db)
    return crud.get_dependents(db, skip, limit)


@org_emp_api.get("/projects")
async def projects(only_count: bool = False, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if only_count:
        return crud.get_projects_count(db)
    return crud.get_projects(db, skip, limit)

