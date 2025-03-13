import pandas as pd
import plotly.express as px

# Bước 1: Đọc dữ liệu
df1 = pd.read_excel(
    "/Users/minhtan/Documents/GitHub/MLinBA/K22416C/Visualization/dataset-416.xlsx",
    sheet_name="Sheet1"
)

# Bước 2: Lọc dữ liệu tiếng Việt và Học Kỳ hợp lệ
df = df1[
    df1["Học Kỳ"].notna()
    & (df1["Ngôn ngữ "] == "TV")  # Đã sửa tên cột
].copy()

# Xử lý cột Học Kỳ
df["Học Kỳ"] = pd.to_numeric(df["Học Kỳ"], errors="coerce")
df = df[df["Học Kỳ"].notna()]
df["Học Kỳ"] = df["Học Kỳ"].astype(int).astype(str)

# Điền giá trị thiếu cho Loại môn học
df["Loại môn học"] = df["Loại môn học"].fillna("Khác")

# Bước 3: Nhóm dữ liệu
grouped = df.groupby(
    ["Học Kỳ", "Loại môn học", "Tên học phần"]
).size().reset_index(name="Số lượng")

# Bước 4: Vẽ sunburst chart
fig = px.sunburst(
    grouped,
    path=["Học Kỳ", "Loại môn học", "Tên học phần"],
    values="Số lượng",
    title="Phân bố môn học theo Học Kỳ, Loại môn học và Tên học phần",
    color="Học Kỳ",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    width=1000,
    height=1000,
)

# Lưu file HTML
fig.write_html("416_10k.html")