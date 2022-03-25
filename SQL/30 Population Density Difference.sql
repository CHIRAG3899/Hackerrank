--Query the difference between the maximum and minimum populations in CITY.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

SELECT MAX(Population) - MIN(Population) AS Joke FROM City;
