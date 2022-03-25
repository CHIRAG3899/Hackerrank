--Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
--The STATION table is described as follows:

--Field	  Type
--ID	  NUMBER
--CITY	  VARCHAR2 (17)
--STATE	  VARCHAR2 (20)
--LAT_N	  NUMBER
--LONG_W  NUMBER


select DISTINCT(CITY) from STATION where (ID%2)=0;