import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc file an toàn hơn
df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1", low_memory=False)

# Tính tổng số vụ theo quốc gia
attacks_by_country = df['country'].value_counts().nlargest(10).reset_index()
attacks_by_country.columns = ['Country', 'Number_of_Attacks']

plt.figure(figsize=(12,6))
sns.barplot(data=attacks_by_country, x='Country', y='Number_of_Attacks', palette='coolwarm')
plt.title('Top 10 quốc gia có số vụ khủng bố nhiều nhất')
plt.xlabel('Quốc gia')
plt.ylabel('Số vụ khủng bố')
plt.xticks(rotation=45, ha='right')  
plt.show()
