CREATE DATABASE TerrorismDB;
GO
CREATE TABLE terrorism_filtered (
    iyear INT,
    imonth INT,
    country NVARCHAR(255),
    region NVARCHAR(255),
    province NVARCHAR(255),
    city NVARCHAR(255),
    weapon NVARCHAR(255),
    weapon_detail NVARCHAR(255),
    deaths INT,
    injured INT
);
SELECT TOP 10 * FROM terrorism_filtered;
--1.Năm nào xảy ra nhiều vụ khủng bố nhất?
SELECT TOP 10 
    iyear, 
    COUNT(*) AS total_attacks
FROM terrorism_filtered
GROUP BY iyear
ORDER BY total_attacks DESC;
--2.Quốc gia nào có nhiều vụ khủng bố nhất?
SELECT TOP 10 
    country, 
    COUNT(*) AS total_attacks
FROM terrorism_filtered
GROUP BY country
ORDER BY total_attacks DESC;
--3.Khu vực nào có số người chết trung bình cao nhất mỗi năm?
SELECT 
    region,
    ROUND(AVG(TRY_CAST(deaths AS FLOAT)), 2) AS avg_deaths_per_attack
FROM terrorism_filtered
WHERE TRY_CAST(deaths AS FLOAT) IS NOT NULL
GROUP BY region
ORDER BY avg_deaths_per_attack DESC;
--4.Loại vũ khí nào được dùng phổ biến nhất?
SELECT TOP 10 
    weapon, 
    COUNT(*) AS used_count
FROM terrorism_filtered
GROUP BY weapon
ORDER BY used_count DESC;
--5.Thành phố nào có nhiều vụ khủng bố nhất?
SELECT TOP 10 
    city, 
    COUNT(*) AS total_attacks
FROM terrorism_filtered
WHERE city <> '0'
GROUP BY city
ORDER BY total_attacks DESC;
--6.Mối quan hệ giữa số người chết và bị thương (trung bình)?
SELECT 
    ROUND(AVG(TRY_CAST(deaths AS FLOAT)), 2) AS avg_deaths,
    ROUND(AVG(TRY_CAST(injured AS FLOAT)), 2) AS avg_injured
FROM terrorism_filtered
WHERE TRY_CAST(deaths AS FLOAT) IS NOT NULL 
  AND TRY_CAST(injured AS FLOAT) IS NOT NULL;
--7.Sự thay đổi của loại vũ khí qua các thập kỷ
SELECT 
    (iyear / 10) * 10 AS decade, 
    weapon, 
    COUNT(*) AS total_attacks
FROM terrorism_filtered
GROUP BY (iyear / 10) * 10, weapon
ORDER BY decade, total_attacks DESC;
--8.Top 10 quốc gia chịu thiệt hại nhân mạng cao nhất
SELECT TOP 10
    country,
    SUM(CAST(deaths AS FLOAT)) AS total_deaths
FROM terrorism_filtered
WHERE ISNUMERIC(deaths) = 1
GROUP BY country
ORDER BY total_deaths DESC;
--9.Sự khác biệt giữa khu vực và loại vũ khí được dùng
SELECT 
    region, 
    weapon, 
    COUNT(*) AS total_attacks
FROM terrorism_filtered
GROUP BY region, weapon
ORDER BY region, total_attacks DESC;
--10.Phân tích xu hướng để dự đoán khu vực dễ xảy ra khủng bố (thống kê)
SELECT 
    region,
    COUNT(*) AS total_attacks,
    SUM(TRY_CAST(deaths AS FLOAT)) AS total_deaths,
    SUM(TRY_CAST(injured AS FLOAT)) AS total_injured
FROM terrorism_filtered
WHERE TRY_CAST(deaths AS FLOAT) IS NOT NULL 
   OR TRY_CAST(injured AS FLOAT) IS NOT NULL
GROUP BY region
ORDER BY total_attacks DESC;



