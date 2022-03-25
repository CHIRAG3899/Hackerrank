--Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than 2000 months. Sort your result by ascending employee_id.

--Input Format
--The Employee table containing employee data for a company is described as follows:

--Field	        Type
--employee_id	Integer
--name	        String
--months	    Integer
--salary	    Integer

--where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

select name from Employee where salary>2000 AND months<10 order by employee_id;