
import pandas as pd
import numpy as np

# --- 1. Đọc file CSV an toàn, tránh lỗi mã hóa ---
# Thử đọc bằng nhiều encoding, tránh lỗi ký tự đặc biệt
try:
    df = pd.read_csv("terrorism_filtered.csv", encoding="utf-8")
except UnicodeDecodeError:
    try:
        df = pd.read_csv("terrorism_filtered.csv", encoding="latin1")
    except:
        df = pd.read_csv("terrorism_filtered.csv", encoding="ISO-8859-1")

# --- Phân tích dữ liệu (theo hướng 10 câu hỏi SQL) ---

print("\n===== 1 Top 10 quốc gia chịu thiệt hại nhân mạng cao nhất =====")
top10_country_deaths = (
    df.groupby('country')['deaths']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top10_country_deaths)

print("\n===== 2️Khu vực có số người chết trung bình cao nhất =====")
avg_deaths_region = (
    df.groupby('region')['deaths']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print(avg_deaths_region)

print("\n===== 3️Mối quan hệ giữa số người chết và bị thương =====")
correlation = df[['deaths', 'injured']].corr()
print(correlation)

print("\n===== 4️Tổng số vụ khủng bố mỗi năm =====")
if 'iyear' in df.columns:
    yearly_attacks = df.groupby('iyear').size()
    print(yearly_attacks.tail(10))
else:
    print("️ Không có cột iyear trong dữ liệu.")

print("\n===== 5️Khu vực nào có số vụ khủng bố cao nhất =====")
region_attacks = df.groupby('region').size().sort_values(ascending=False).head(10)
print(region_attacks)

print("\n===== 6️⃣ Top 5 loại vũ khí gây thương vong cao nhất =====")
if 'weapon' in df.columns:
    df['casualties'] = df['deaths'] + df['injured']  # tổng thương vong
    top5_weapon_casualties = (
        df.groupby('weapon')['casualties']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    print(top5_weapon_casualties)
else:
    print(" Không có cột weapon trong dữ liệu.")


print("\n===== 7  Vũ khí phổ biến nhất được sử dụng =====")
if 'weapon' in df.columns:
    weapon_count = df.groupby('weapon').size().sort_values(ascending=False).head(5)
    print(weapon_count)
else:
    print(" Không có cột weapon trong dữ liệu.")

print("\n===== 8️Trung bình mỗi vụ có bao nhiêu người chết/bị thương =====")
avg_deaths = df['deaths'].mean()
avg_injured = df['injured'].mean()
print(f"Trung bình mỗi vụ có {avg_deaths:.2f} người chết và {avg_injured:.2f} người bị thương.")

print("\n===== 9️Năm mới nhất và năm cũ nhất trong dữ liệu =====")
if 'iyear' in df.columns:
    print("Năm cũ nhất:", df['iyear'].min())
    print("Năm mới nhất:", df['iyear'].max())

print("\n=====  Phân tích xu hướng tổng hợp =====")
trend = (
    df.groupby('region')[['deaths', 'injured']]
    .sum()
    .sort_values(by='deaths', ascending=False)
)
print(trend.head(10))




