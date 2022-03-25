--Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.
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

SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;