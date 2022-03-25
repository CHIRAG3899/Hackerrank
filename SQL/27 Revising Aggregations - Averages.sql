--Query the average population of all cities in CITY where District is California.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

select avg(population)
from city 
where district = 'California';
