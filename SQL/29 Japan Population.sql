--Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

--Input Format
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE ='JPN';
