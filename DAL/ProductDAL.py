import os

from libs.JsonFileFactory import JsonFileFactory
from model.Product import Product


class ProductDAL:
    def __init__(self):
        self.list_product = []
        self.json_factory = JsonFileFactory()
    def add(self, new_emp):
        self.list_product.append(new_emp)
    def get_filepath(self, filepath):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, filepath)
        return str(filepath)
    def get_all_products(self):
        filepath = self.get_filepath("../dataset/product.json")
        self.list_product = self.json_factory.read_data(filepath, Product)
        return self.list_product
    def store_new_product(self, new_product):
        filepath = self.get_filepath("../dataset/product.json")
        self.list_product = self.get_all_products()
        self.add(new_product)
        self.json_factory.write_data(self.list_product, filepath)
    def get_product_by_id(self, arrData, id):
        temp_product = None
        for data in arrData:
            if data.id == id:
                temp_product = data
                break
        return temp_product
    def get_index_product_by_id(self, id, arrData):
        temp_index = None
        for i in range(len(arrData)):
            if arrData[i].id == id:
                temp_index = i
                break
        return temp_index
    def update_new_product(self, update_product):
        filepath = self.get_filepath("../dataset/product.json")
        list_product = self.get_all_products()
        index_update = self.get_index_product_by_id(update_product.id, list_product)
        list_product[index_update] = update_product
        self.json_factory.write_data(list_product, filepath)
    def delete_product(self, id):
        filepath = self.get_filepath("../dataset/product.json")
        list_product= self.get_all_products()
        index_delete = self.get_index_product_by_id(id, list_product)
        del list_product[index_delete]
        self.json_factory.write_data(list_product, filepath)
    def update_quantity_selling(self, quantity, product_need):
        filepath = self.get_filepath("../dataset/product.json")
        product_need.quantity -= quantity
        list_product = self.get_all_products()
        index_update = self.get_index_product_by_id(product_need.id, list_product)
        list_product[index_update] = product_need
        self.json_factory.write_data(list_product, filepath)
    def update_quantity_recover(self, quantity, product_need):
        filepath = self.get_filepath("../dataset/product.json")
        product_need.quantity += quantity
        list_product = self.get_all_products()
        index_update = self.get_index_product_by_id(product_need.id, list_product)
        list_product[index_update] = product_need
        self.json_factory.write_data(list_product, filepath)
    def search(self, category, sub_category, product_name):
        list_product = self.get_all_products()
        temp_product = None
        for product in list_product:
            if product.category == category and product.sub_category == sub_category and product.name == product_name:
                temp_product = product
                break
        return temp_product