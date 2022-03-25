--Query the average population for all cities in CITY, rounded down to the nearest integer.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

select Round(avg(population)) from city;
