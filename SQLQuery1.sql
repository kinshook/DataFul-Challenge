CREATE DATABASE codebasics_ch
USE codebasics_ch


SELECT * FROM aqi_datasets_copy

SELECT * INTO aqi_staging FROM aqi_datasets_copy WHERE 1 = 0;

INSERT INTO aqi_staging
SELECT * FROM aqi_datasets_copy;

SELECT * FROM aqi_staging

ALTER TABLE aqi_staging
DROP COLUMN column8;

SELECT SUM(aqi_value) FROM aqi_staging
WHERE area = 'Byrnihat'AND (date>='2024-12-01' AND date<='2025-05-31')

SELECT YEAR(date), state, AVG(Cast(aqi_value AS float)) as avg_state FROM aqi_staging
GROUP BY YEAR(date), state
ORDER BY  YEAR(date),avg_state

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY aqi_value) OVER() as avg_aqi FROM aqi_staging

SELECT ROUND(AVG(CAST(aqi_value AS FLOAT)),2),COUNT(date) FROM aqi_staging
WHERE YEAR(date)=2024


SELECT COUNT(date) as counts FROM aqi_staging
WHERE YEAR(date)=2022

SELECT COUNT(*) FROM aqi_staging WHERE YEAR(date) = 2022;

