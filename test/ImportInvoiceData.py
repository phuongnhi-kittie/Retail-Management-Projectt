import json
import random
from datetime import datetime, timedelta

# Load product data from previous generated list
product_file_path = f"../dataset/product.json"

with open(product_file_path, "r", encoding="utf-8") as f:
    products = json.load(f)

product_ids = [product["id"] for product in products]

# Danh sách mẫu tên họ
first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Bui", "Dang", "Do", "Ngo", "Vu"]
middle_names = ["Van", "Phuong", "Anh", "Ngoc", "Quoc", "Thanh", "Duy", "Minh", "Bao", "Thi"]
last_names = ["Sang", "Thao", "Tai", "Thu", "Linh", "Duc", "Hieu", "Nhi", "Khoa", "Trang"]


# Generate invoices
invoices = []
for i in range(1, 201):  # 200 invoices
    first_name = first_names[i % len(first_names)]
    middle_name = middle_names[i % len(middle_names)]
    last_name = last_names[i % len(last_names)]
    date = (datetime(2025, 3, 1) + timedelta(days=random.randint(0, 30))).strftime("%d/%m/%Y")
    customer_name = f"{first_name} {middle_name} {last_name}"
    phone = f"0{random.randint(100000000, 999999999)}"

    # Generate list of purchased products (2-10 items per invoice)
    num_products = random.randint(3, 10)
    list_product = random.sample(product_ids, num_products)
    list_product = [[prod_id, random.randint(1, 20)] for prod_id in list_product]

    invoice = {
        "bill_no": f"bill{i}",
        "date": date,
        "customer_name": customer_name,
        "phone": phone,
        "list_product": list_product
    }
    invoices.append(invoice)

# Save invoices to JSON file
invoice_file_path = f"../dataset/invoice.json"
with open(invoice_file_path, "w", encoding="utf-8") as f:
    json.dump(invoices, f, indent=4, ensure_ascii=False)

invoice_file_path
