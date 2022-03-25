--Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
--The CITY table is described as follows:

--Field	  Type
--ID	  NUMBER
--CITY	  VARCHAR2 (17)
--STATE	  VARCHAR2 (20)
--LAT_N	  NUMBER
--LONG_W  NUMBER


SELECT CITY,STATE FROM STATION;