import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1", low_memory=False)

# Lọc dữ liệu trong 10 năm gần nhất
df_recent = df[(df['iyear'] >= 2007) & (df['iyear'] <= 2017)]

# Nhóm dữ liệu theo năm và khu vực, tính tổng số người chết
regional_deaths = df_recent.groupby(['iyear', 'region'])['deaths'].sum().unstack()

# Vẽ biểu đồ cột chồng
plt.figure(figsize=(14, 7))
regional_deaths.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab20')
plt.title('Tỷ trọng thiệt hại (số người chết) theo khu vực và năm (2007–2017)', fontsize=14, weight='bold')
plt.xlabel('Năm')
plt.ylabel('Tổng số người chết')
plt.legend(title='Khu vực', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
