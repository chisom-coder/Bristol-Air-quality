SELECT 
  stations.SiteID,
  stations.Location, 
  AVG(readings.`PM2.5`) AS mean_pm2_5,
  AVG(readings.`VPM2.5`) AS mean_VPM2_5
FROM readings
JOIN stations ON readings.`Stationid` = stations.`SiteID` 
WHERE 
  YEAR(readings.`Date Time`) = 2019
  AND TIME(readings.`Date Time`) = '08:00:00'
GROUP BY
  readings.`Stationid`;
