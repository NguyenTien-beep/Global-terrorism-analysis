import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1", low_memory=False)

df_recent = df[(df['iyear'] >= 2007) & (df['iyear'] <= 2017)]

# Tính tổng số người chết mỗi năm cho từng khu vực
region_deaths = df_recent.groupby(['iyear', 'region'])['deaths'].sum().unstack()

# Tính ma trận tương quan giữa các khu vực
corr_matrix = region_deaths.corr()

# Vẽ heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Ma trận tương quan thiệt hại giữa các khu vực (2007–2017)', fontsize=14, weight='bold')
plt.text(
    x=9.5, y=1700,
    s=("Nhận xét:\n"
       "- Điểm tròn: vụ cực kỳ nghiêm trọng."),
    fontsize=10,
    color='black',
    bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5'))
plt.show()
# Màu đỏ = Hai khu vực “thiệt hại cùng tăng cùng giảm”.

# Màu xanh = Hai khu vực “thiệt hại ngược chiều nhau”.

# Màu nhạt = “Không liên quan rõ”.