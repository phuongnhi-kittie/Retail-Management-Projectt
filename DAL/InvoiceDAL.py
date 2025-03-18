import os

from PyQt6.QtWidgets import QMessageBox

from libs.JsonFileFactory import JsonFileFactory
from model.Invoice import Invoice


class InvoiceDAL:
    def __init__(self):
        self.list_invoice = []
        self.json_factory = JsonFileFactory()
    def add(self, new_bill):
        self.list_invoice.append(new_bill)
    def get_filepath(self, filepath):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, filepath)
        return str(filepath)
    def get_all_invoices(self):
        filepath = self.get_filepath("../dataset/invoice.json")
        self.list_invoice = self.json_factory.read_data(filepath, Invoice)
        return self.list_invoice
    def get_invoice_by_id(self, id):
        list_invoice = self.get_all_invoices()
        temp_invoice = None
        for invoice in list_invoice:
            if invoice.bill_no == id:
                temp_invoice = invoice
                break
        return temp_invoice
    def delete_invoice(self, id):
        filename = self.get_filepath("../dataset/invoice.json")
        deleted_invoice = self.get_invoice_by_id(id)
        self.list_invoice.remove(deleted_invoice)
        self.json_factory.write_data(self.list_invoice, filename)
        msg = QMessageBox()
        msg.setText("Delete successfully")
        msg.setWindowTitle("Announcement !!!")
        msg.exec()
    def store_new_bill(self, new_bill):
        filepath = self.get_filepath("../dataset/invoice.json")
        self.list_invoice = self.get_all_invoices()
        self.add(new_bill)
        self.json_factory.write_data(self.list_invoice, filepath)