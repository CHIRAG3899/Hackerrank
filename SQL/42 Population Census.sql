--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

--Input Format
--The CITY and COUNTRY tables are described as follows:

--Field	        Type
--ID	        NUMBER
--NAME	        VARCHAR
--COUNTRYCODE	VARCHAR
--DISTRICT	    VARCHAR
--POPULATION	NUMBER

--Field	          Type
--CODE	          VARCHAR
--NAME	          VARCHAR
--CONTINENT	      VARCHAR
--REGION	      VARCHAR
--SURFACEAREA	  NUMBER
--INDEPYEAR	      VARCHAR
--POPULATION	  NUMBER
--LIFEEXPECTANCY  VARCHAR
--GNP	          NUMBER
--GNPOLD	      VARCHAR
--LOCALNAME	      VARCHAR
--GOVERNMENTFORM  VARCHAR
--HEADOFSTATE	  VARCHAR
--CAPITAL	      VARCHAR
--CODE2	          VARCHAR

SELECT SUM(CITY.POPULATION) 
FROM CITY, COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE AND COUNTRY.CONTINENT = 'Asia';