--Query the total population of all cities in CITY where District is California.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

SELECT SUM(Population)
FROM City
WHERE District = 'California';
