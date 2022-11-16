from sqlalchemy.orm import Session
from . import models, schemas


def get_employee_count(db: Session):
    return db.query(models.Employee).count()

def get_full_time_employee_count(db: Session):
    return db.query(models.SalaryEmployee).count()

def get_contract_employee_count(db: Session):
    return db.query(models.HourlyEmployee).count()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_filtered_employees(db: Session, filter_val: str = None, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.employee_id.ilike(f'%{filter_val}%')).offset(skip).limit(limit).all()

def get_fulltime_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).join(models.SalaryEmployee, models.Employee.employee_id == models.SalaryEmployee.employee_id).offset(skip).limit(limit).all()

def get_contract_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).join(models.HourlyEmployee, models.Employee.employee_id == models.HourlyEmployee.employee_id).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: str):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()

def get_employee_ssn(db: Session, ssn: int):
    return db.query(models.Employee).filter(models.Employee.ssn == ssn).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, db_employee: schemas.EmployeeCreate, employee: schemas.EmployeeCreate):
    employee = employee.__dict__
    for key, value in employee.items():
        setattr(db_employee, key, value)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, db_employee: schemas.EmployeeCreate):
    db.delete(db_employee)
    db.commit()
    return db_employee






def get_dependent_count(db: Session):
    return db.query(models.Dependent).count()

def get_dependents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dependent).offset(skip).limit(limit).all()

def get_employee_dependents(db: Session, employee_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Dependent).filter(models.Dependent.employee_id == employee_id).offset(skip).limit(limit).all()

def get_employee_dependent(db: Session, employee_id: str, dependent_id: str):
    return db.query(models.Dependent).filter(models.Dependent.employee_id == employee_id, models.Dependent.dependent_id == dependent_id).first()

def create_employee_dependent(db: Session, dependent: schemas.DependentCreate):
    db_dept = models.Dependent(**dependent.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def update_employee_dependent(db: Session, db_depndt: schemas.DependentCreate, dependent: schemas.DependentCreate):
    dependent = dependent.__dict__
    for key, value in dependent.items():
        setattr(db_depndt, key, value)
    db.add(db_depndt)
    db.commit()
    db.refresh(db_depndt)
    return db_depndt

def delete_employee_dependent(db: Session, db_depndt: models.Dependent):
    db.delete(db_depndt)
    db.commit()
    return db_depndt






def get_department_count(db: Session):
    return db.query(models.Department).count()

def get_department(db: Session, department_number: str):
    return db.query(models.Department).filter(models.Department.department_number == department_number).first()


def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()


def create_department(db: Session, department: schemas.DepartmentCreate):
    db_dept = models.Department(**department.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def update_department(db: Session, db_dept: schemas.DepartmentCreate, department: schemas.DepartmentCreate):
    department = department.__dict__
    for key, value in department.items():
        setattr(db_dept, key, value)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def delete_department(db: Session, db_dept: models.Department):
    db.delete(db_dept)
    db.commit()
    return db_dept








def get_projects_count(db: Session):
    return db.query(models.Project).count()

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def get_department_projects(db: Session, department_number: str):
    return db.query(models.Employee).filter(models.Project.department_number == department_number).first()

def get_department_project(db: Session, department_number: str, project_id: str):
    return db.query(models.Employee).filter(models.Project.project_id == project_id, models.Project.department_number == department_number).first()


def create_department_project(db: Session, project: schemas.ProjectCreate):
    db_dept_prjct = models.Department(**project.dict())
    db.add(db_dept_prjct)
    db.commit()
    db.refresh(db_dept_prjct)
    return db_dept_prjct

def update_department(db: Session, db_dept_prjct: schemas.ProjectCreate, project: schemas.ProjectCreate):
    department = department.__dict__
    for key, value in department.items():
        setattr(db_dept_prjct, key, value)
    db.add(db_dept_prjct)
    db.commit()
    db.refresh(db_dept_prjct)
    return db_dept_prjct

def delete_department(db: Session, db_dept_prjct: models.Department):
    db.delete(db_dept_prjct)
    db.commit()
    return db_dept_prjct