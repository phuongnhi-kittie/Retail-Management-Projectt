import json
import random

# Danh mục sản phẩm và từ khóa tương ứng để phân loại
categories = {
    "Đồ chơi xếp hình":  [
        "Bộ xếp hình sáng tạo 1000 chi tiết",
        "Lego kỹ thuật cao cấp",
        "Bộ xếp hình lâu đài cổ tích",
        "Xếp hình 3D mô hình thành phố",
        "Bộ xếp hình xe hơi thông minh"
    ],
    "Đồ chơi giáo dục":  [
        "Bảng chữ cái điện tử",
        "Bộ toán học thông minh",
        "Bộ cờ vua nam châm cao cấp",
        "Bảng học vẽ cho bé",
        "Bộ flashcard thông minh"
    ],
    "Đồ chơi điều khiển từ xa":  [
        "Ô tô địa hình điều khiển từ xa",
        "Máy bay trực thăng mini",
        "Robot chiến đấu AI",
        "Xe đua tốc độ cao",
        "Tàu thủy điều khiển từ xa"
    ],
    "Đồ chơi ngoài trời": [
        "Xe trượt scooter 3 bánh",
        "Cầu trượt cho bé 2m",
        "Bập bênh hình con thú",
        "Bộ nhà banh mini",
        "Xích đu lắp ghép"
    ],
    "Đồ chơi búp bê & mô hình":  [
        "Búp bê công chúa phát nhạc",
        "Bộ mô hình siêu nhân",
        "Bộ đồ chơi nhà búp bê",
        "Mô hình xe hơi tĩnh cao cấp",
        "Bộ sưu tập mô hình khủng long"
    ],
    "Đồ chơi âm nhạc": [
        "Đàn piano điện tử mini",
        "Guitar gỗ trẻ em",
        "Trống điện tử đa năng",
        "Bộ nhạc cụ 5 món cho bé",
        "Đàn organ phát sáng"
    ],
    "Đồ chơi cho bé sơ sinh":  [
        "Lục lạc hình thú dễ thương",
        "Xúc xắc nhiều màu sắc",
        "Bộ đồ chơi treo nôi phát nhạc",
        "Thảm nằm chơi cho bé",
        "Bộ cắn răng an toàn"
    ]
}

# Sinh ngẫu nhiên danh sách sản phẩm
products = []
for i in range(1, 370):  # 369 sản phẩm
    category = random.choice(list(categories.keys()))
    name = random.choice(categories[category])
    sub_category = "".join(word[0].lower() for word in category.split()) #viết tắt các chữ cái đầu của category
    cost_price = round(random.uniform(50000, 200000), 2)  # Giá nhập từ 50k đến 300k
    selling_price = round(cost_price * random.uniform(1.2, 1.5), 2)  # Giá bán luôn cao hơn
    product = {
        "id": f"prod{i}",
        "name": name,
        "category": category,
        "sub_category": sub_category,
        "quantity": random.randint(8000, 12000),
        "cost_price": cost_price,
        "selling_price": selling_price,
        "vendor_phone": f"0{random.randint(100000000, 999999999)}"
    }
    products.append(product)

# Lưu vào file JSON
file_path = f"../dataset/product.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

file_path
