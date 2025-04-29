import pandas as pd
import ast  # Để chuyển đổi chuỗi list thành list thật

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("pokemon_data.csv")

# Chuyển chuỗi list (ví dụ: "['grass', 'poison']") thành list Python thật sự
df["type"] = df["type"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("[") else [x])

# Lọc các Pokémon có 'poison' trong danh sách type
poison_pokemon = df[df["type"].apply(lambda x: "poison" in [t.lower() for t in x])]

# Hiển thị kết quả
print("Các Pokémon có loại 'poison':")
print(poison_pokemon[["number", "name", "type"]])