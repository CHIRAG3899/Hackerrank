--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.

--Input Format
--The STATION table is described as follows:

--Field	  Type
--ID	  NUMBER
--CITY	  VARCHAR2 (17)
--STATE	  VARCHAR2 (20)
--LAT_N	  NUMBER
--LONG_W  NUMBER

--where LAT_N is the northern latitude and LONG_W is the western longitude.

Select ROUND(LONG_W,4) from STATION WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);