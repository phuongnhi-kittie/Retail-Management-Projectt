import os

from libs.JsonFileFactory import JsonFileFactory
from model.Employee import Employee


class EmployeeDAL:
    def __init__(self):
        self.list_employee = []
        self.json_factory = JsonFileFactory()
    def add(self, new_emp):
        self.list_employee.append(new_emp)
    def get_filepath(self, filepath):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, filepath)
        return str(filepath)
    def get_all_employee(self):
        filepath = self.get_filepath("../dataset/user.json")
        self.list_employee = self.json_factory.read_data(filepath, Employee)
        return self.list_employee
    def store_new_employee(self, new_emp):
        filepath = self.get_filepath("../dataset/user.json")
        self.list_employee = self.get_all_employee()
        self.add(new_emp)
        self.json_factory.write_data(self.list_employee, filepath)
    def get_emp_by_id(self, arrData, id):
        temp_emp = None
        for data in arrData:
            if data.id == id:
                temp_emp = data
                break
        return temp_emp
    def get_index_emp_by_id(self, id, arrData):
        temp_index = None
        for i in range(len(arrData)):
            if arrData[i].id == id:
                temp_index = i
                break
        return temp_index
    def update_new_employee(self, update_emp):
        filepath = self.get_filepath("../dataset/user.json")
        list_emp = self.get_all_employee()
        index_update = self.get_index_emp_by_id(update_emp.id, list_emp)
        list_emp[index_update] = update_emp
        self.json_factory.write_data(list_emp, filepath)
    def delete_emp(self, id):
        filepath = self.get_filepath("../dataset/user.json")
        list_emp = self.get_all_employee()
        index_delete = self.get_index_emp_by_id(id, list_emp)
        del list_emp[index_delete]
        self.json_factory.write_data(list_emp, filepath)
