--Query a count of the number of cities in CITY having a Population larger than 100000.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

SELECT COUNT(ID) FROM CITY WHERE POPULATION>100000;
