import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Đọc file an toàn
df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1", low_memory=False)

# Tạo biểu đồ phân tán
plt.figure(figsize=(8,8))
sns.scatterplot(data=df, x='deaths', y='injured', alpha=0.5)
plt.title('Mối quan hệ giữa số người chết và số người bị thương')
plt.xlabel('Số người chết (deaths)')
plt.ylabel('Số người bị thương (injured)')
plt.show()
