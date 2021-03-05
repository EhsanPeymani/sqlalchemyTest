from sqlalchemy.orm import Session
from models import *

def PrintEmployeeCustomers(session, doIt=True):
    if (not doIt):
        return
    employees = session.query(Employee).all()

    for emp in employees:
        if len(emp.Customers) > 0:
            emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName}"
            print(f"{emp_name}:")
            for cust in emp.Customers:
                cust_name = "".ljust(10) + f"{cust.FirstName} {cust.LastName}"
                print(cust_name)

def PrintManagerEmployees(session, doIt=True):
    if (not doIt):
        return;

    employees = session.query(Employee).all()
    for emp in employees:
        emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName} ({len(emp.ReportingEmployees)})"
        emp_name_reports_to = emp_name.ljust(30) + "reports to "
        if emp.Manager is not None:
            print(emp_name_reports_to + f"{emp.Manager.FirstName} {emp.Manager.LastName} ({len(emp.Manager.ReportingEmployees)}) -> {emp.ReportingManager.LastName}")
        else:
            print(emp_name)
    
