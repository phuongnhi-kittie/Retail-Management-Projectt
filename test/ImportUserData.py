import json
import random
# Danh sách các chức vụ có sẵn
designations = [
    "System Administrator (IT Manager)",
    "Store Manager",
    "Accountant",
    "Employee"
]

# Danh sách các địa chỉ mẫu
addresses = ["Binh Duong", "Tp. Ho Chi Minh", "Da Nang", "Hai Phong", "Ha Noi", "Can Tho", "Nha Trang", "Vung Tau"]

# Danh sách mẫu tên họ
first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Bui", "Dang", "Do", "Ngo", "Vu"]
middle_names = ["Van", "Phuong", "Anh", "Ngoc", "Quoc", "Thanh", "Duy", "Minh", "Bao", "Thi"]
last_names = ["Sang", "Thao", "Tai", "Thu", "Linh", "Duc", "Hieu", "Nhi", "Khoa", "Trang"]

# Tạo danh sách user
users = []
for i in range(1, 127):
    first_name = first_names[i % len(first_names)]
    middle_name = middle_names[i % len(middle_names)]
    last_name = last_names[i % len(last_names)]

    user = {
        "id": f"emp{i}",
        "name": f"{first_name} {middle_name} {last_name}",
        "phone": f"0{random.randint(100000000, 999999999)}",  # Tạo số điện thoại ngẫu nhiên
        "designation": designations[i % len(designations)],
        "address": addresses[i % len(addresses)],
        "username": f"{first_name.lower()}{last_name.lower()}{i}",
        "password": "hellokitty"
    }
    users.append(user)

# Lưu vào file JSON
file_path = f"../dataset/user.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(users, f, indent=4, ensure_ascii=False)

file_path
