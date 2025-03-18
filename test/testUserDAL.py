from DAL.UserDAL import EmployeeDAL

emp_dal = EmployeeDAL()
list_emp = emp_dal.get_all_employee()
for emp in list_emp:
    print(emp)