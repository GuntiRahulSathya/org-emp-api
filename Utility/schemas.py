import datetime
import random, string, uuid
from typing import Optional
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    ssn: int
    employee_id: str = 'emp-'+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    dob: datetime.date
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zipcode: Optional[str] = None
    department_number: str
    join_date: datetime.date = str(datetime.datetime.utcnow().date())
    job_title: str = None

    class Config:
        orm_mode = True


class SalaryEmployeeBase(BaseModel):
    employee_id: Optional[str] = None
    salary: Optional[str] = None
    bonus: Optional[float] = None

    class Config:
        orm_mode = True


class HourlyEmployeeBase(BaseModel):
    employee_id: str
    hourly_salary: int
    bonus: Optional[float] = None

    class Config:
        orm_mode = True


class DependentBase(BaseModel):
    dependent_id: str = 'depndt-' + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    dependent_name: str
    dependent_relation: str
    employee_id: str

    class Config:
        orm_mode = True


class DepartmentBase(BaseModel):
    department_number: str = 'dept-' + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    department_name: str
    manager_id: str
    location_id: Optional[str] = None

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    location_id: str = 'loc-' + str(uuid.uuid4())
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zipcode: Optional[str] = None

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    project_number: str = 'prjct-' + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    project_name: str
    project_description: Optional[str] = None
    department_number: str

    class Config:
        orm_mode = True


class EmployeeProjectBase(BaseModel):
    employee_id: str
    project_number: str
    start_date: datetime.date = None
    end_date: Optional[datetime.date] = None
    hours: Optional[float] = None

    class Config:
        orm_mode = True





class EmployeeCreate(EmployeeBase):
    pass

class DepartmentCreate(DepartmentBase):
    pass

class DependentCreate(DependentBase):
    pass

class ProjectCreate(ProjectBase):
    pass