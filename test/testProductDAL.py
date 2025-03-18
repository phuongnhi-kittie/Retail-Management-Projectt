from DAL.ProductDAL import ProductDAL

product_dal = ProductDAL()
list_product = product_dal.get_all_products()
for product in list_product:
    print(product)