--Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--COUNTRY CODE	VARCHAR2 (17)
--DISTRICT	    VARCHAR2(20)
--POPULATION	NUMBER

SELECT * FROM CITY WHERE COUNTRYCODE='JPN';