import pandas as pd
import requests
from io import BytesIO

# Tải file Excel từ Google Sheets
url = "https://docs.google.com/spreadsheets/d/1BnOzoEG0s6c8MpiUANZ0_pawXNHqdkid/export?format=xlsx"
response = requests.get(url)

# Đọc dữ liệu từ file Excel
data = pd.read_excel(BytesIO(response.content))

# Chuyển đổi các cột cần thiết sang số (nếu không phải số)
for col in ['vpv2', 'pDisCharge', 'prec', 'vBus1', 'vBus2']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Lọc dữ liệu: vpv2 và pDisCharge chẵn, prec lẻ
filtered_data = data[
    (data['vpv2'] % 2 == 0) &
    (data['pDisCharge'] % 2 == 0) &
    (data['prec'] % 2 == 1)
]

# Thêm cột mới Sum_vBUS = vBus1 + vBus2
filtered_data['Sum_vBUS'] = filtered_data['vBus1'] + filtered_data['vBus2']

# Lưu kết quả vào file CSV
filtered_data.to_csv("Data_new.csv", index=False, encoding='utf-8-sig')

print("✅ Đã xử lý xong và lưu vào Data_new.csv")
