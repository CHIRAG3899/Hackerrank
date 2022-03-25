--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
--The CITY table is described as follows:

--Field	        Type
--ID	        NUMBER
--COUNTRY CODE	VARCHAR2 (17)
--DISTRICT	    VARCHAR2(20)
--POPULATION	NUMBER

SELECT NAME FROM CITY WHERE POPULATION>=120000 AND COUNTRYCODE='USA';