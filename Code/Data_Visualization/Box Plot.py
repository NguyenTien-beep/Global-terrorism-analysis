import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1", low_memory=False)

# Lọc dữ liệu 10 năm gần nhất (2007–2017)
df_recent = df[(df['iyear'] >= 2007) & (df['iyear'] <= 2017)]

# Vẽ Box Plot
plt.figure(figsize=(12,7))
ax = sns.boxplot(data=df_recent, x='region', y='deaths', palette='Reds')

plt.title('Phân bố số người chết giữa các khu vực (2007–2017)', fontsize=14, weight='bold')
plt.xlabel('Khu vực (Region)')
plt.ylabel('Số người chết (deaths)')
plt.xticks(rotation=45, ha='right')

# Hộp ghi chú góc phải
plt.text(
    x=9.5, y=1700,
    s=("Nhận xét:\n"
       "- Điểm tròn: vụ cực kỳ nghiêm trọng."),
    fontsize=10,
    color='black',
    bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5')
)

plt.show()
