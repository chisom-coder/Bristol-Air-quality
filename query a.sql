SELECT stations.Location, MAX(readings.NOx), readings.`Date Time` AS date
FROM readings
JOIN stations ON readings.Stationid = stations.SiteID
WHERE YEAR(`Date Time`) = '2022' AND NOx IN (SELECT MAX(NOx) FROM readings WHERE YEAR(`Date Time`) = '2022')
GROUP BY stations.Location, `Date Time`;