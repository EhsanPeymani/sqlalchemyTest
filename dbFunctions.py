from sqlalchemy.orm import Session
from models import *

class Functions:
    def __init__(self, session):
        self.session = session

    def PrintEmployeeCustomers(self, doIt=False):
        if (not doIt):
            return
        employees = self.session.query(Employee).all()

        for emp in employees:
            if len(emp.Customers) > 0:
                emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName}"
                print(f"{emp_name}:")
                for cust in emp.Customers:
                    cust_name = "".ljust(10) + f"{cust.FirstName} {cust.LastName}"
                    print(cust_name)

    def PrintManagerEmployees(self, doIt=False):
        if (not doIt):
            return;

        employees = self.session.query(Employee).all()
        for emp in employees:
            emp_name = f"{emp.EmployeeId} - {emp.FirstName} {emp.LastName} ({len(emp.ReportingEmployees)})"
            emp_name_reports_to = emp_name.ljust(30) + "reports to "
            if emp.Manager is not None:
                print(emp_name_reports_to + f"{emp.Manager.FirstName} {emp.Manager.LastName} ({len(emp.Manager.ReportingEmployees)}) -> {emp.ReportingManager.LastName}")
            else:
                print(emp_name)

    def PrintCustomerSupports(self, doIt=False):
        if (not doIt):
            return

        customers = self.session.query(Customer).all()
        for customer in customers:
            print(f"{customer.FirstName} {customer.LastName}".ljust(30), f"{len(customer.Invoices)}".ljust(5), "<--", 
                f"{customer.SupportEmployee.FirstName} {customer.SupportEmployee.LastName}")
    
