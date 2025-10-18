import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('terrorism_filtered.csv', encoding='latin1')

# Chuẩn hóa tên cột 
df.columns = df.columns.str.strip()

# Dùng cột iyear làm cột năm
df['Year'] = df['iyear']

# -------------------------------
# Biểu đồ xu hướng số người chết theo năm
# -------------------------------
yearly_deaths = df.groupby('Year')['deaths'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=yearly_deaths, x='Year', y='deaths', marker='o', color='red')
plt.title(' Xu hướng Số người chết do Khủng bố theo Năm')
plt.xlabel('Năm')
plt.ylabel('Số người chết')
plt.show()

# -------------------------------
# Biểu đồ Top 10 nhóm khủng bố gây chết người nhiều nhất
if 'group_name' in df.columns:
    top_groups = df.groupby('group_name')['deaths'].sum().nlargest(10).reset_index()

    plt.figure(figsize=(10,6))
    sns.barplot(data=top_groups, x='deaths', y='group_name', palette='Reds_r')
    plt.title('Top 10 Nhóm Khủng Bố Gây Chết Người Nhiều Nhất')
    plt.xlabel('Số người chết')
    plt.ylabel('Nhóm khủng bố')
    plt.show()
else:
    print(" Không tìm thấy cột 'group_name' trong dữ liệu.")
    


