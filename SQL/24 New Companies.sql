--Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

-- Founder-->Lead Manager-->Senior Manager-->Manager-->Employee

--Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

--Note:
--The tables may contain duplicate records.
--The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

--Input Format
--The following tables contain company data:

--Company: The company_code is the code of the company and founder is the founder of the company.

--Field	        Type
--company_code	String
--founder	    String

--Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.

--Field	            Type
--company_code	    String
--Lead_Manager_Code	String

--Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

--Field	                Type
--company_code	        String
--Lead_Manager_Code	    String
--Senior_Manager_Code	String

--Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

--Field	               Type
--company_code	       String
--Lead_Manager_Code	   String
--Senior_Manager_Code  String
--Manager_Code	       String

--Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

--Field	                Type
--company_code	        String
--Lead_Manager_Code	    String
--Senior_Manager_Code	String
--Manager_Code	        String
--employee_code	        String

select c.COMPANY_CODE, c.FOUNDER, COUNT(DISTINCT LEAD_MANAGER_CODE), COUNT(DISTINCT SENIOR_MANAGER_CODE), COUNT(DISTINCT MANAGER_CODE), COUNT(DISTINCT EMPLOYEE_CODE)
from EMPLOYEE 
join company c on employee.company_code = c.company_code
group by c.company_code, c.founder
order by c.COMPANY_CODE;



