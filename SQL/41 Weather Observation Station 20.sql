--A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

--Input Format
--The STATION table is described as follows:

--Field	  Type
--ID	  NUMBER
--CITY	  VARCHAR2 (17)
--STATE	  VARCHAR2 (20)
--LAT_N	  NUMBER
--LONG_W  NUMBER

--where LAT_N is the northern latitude and LONG_W is the western longitude.

select ROUND(LAT_N,4) from (SELECT LAT_N FROM STATION ORDER BY 1 asc LIMIT 250) s ORDER BY 1 DESC LIMIT 1;
