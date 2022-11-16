from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = "employee"

    ssn = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zipcode = Column(String)
    department_number = Column(String, ForeignKey("department.department_number"))
    join_date = Column(Date)
    job_title = Column(String)
    dependent = relationship("Dependent", cascade="all, delete")
    contractemp = relationship("HourlyEmployee", cascade="all, delete")
    fulltimeemp = relationship("SalaryEmployee", cascade="all, delete")


class Dependent(Base):
    __tablename__ = "dependent"

    dependent_id = Column(String, primary_key=True, index=True)
    dependent_name =  Column(String)
    dependent_relation =  Column(String)
    employee_id =  Column(String, ForeignKey("employee.employee_id"))


class HourlyEmployee(Base):
    __tablename__ = "hourly_employee"

    employee_id = Column(String, ForeignKey("employee.employee_id"), primary_key=True, index=True)
    hourly_salary = Column(Integer)
    bonus =  Column(Float)


class SalaryEmployee(Base):
    __tablename__ = "salary_employee"

    employee_id =  Column(String, ForeignKey("employee.employee_id"), primary_key=True, index=True)
    salary =  Column(String)
    bonus =  Column(Float)


class Department(Base):
    __tablename__ = "department"

    department_number = Column(String, primary_key=True, index=True)
    department_name = Column(String)
    manager_id = Column(String, ForeignKey("employee.employee_id"))
    location_id = Column(String, ForeignKey("location.location_id"))
    project = relationship("Project", cascade="all, delete")


class Location(Base):
    __tablename__ = "location"

    location_id = Column(String, primary_key=True, index=True)
    address1 =  Column(String)
    address2 =  Column(String)
    city =  Column(String)
    state =  Column(String)
    country =  Column(String)
    zipcode =  Column(String)


class Project(Base):
    __tablename__ = "project"

    project_number = Column(String, primary_key=True, index=True)
    project_name = Column(String)
    project_description =  Column(String)
    department_number = Column(String, ForeignKey("department.department_number"))
    emp_project = relationship("EmployeeProject", cascade="all, delete")


class EmployeeProject(Base):
    __tablename__ = "employee_projects"

    employee_id = Column(String, ForeignKey("employee.employee_id"), primary_key=True, index=True)
    project_number = Column(String, ForeignKey("project.project_number"), primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    hours =  Column(Float)