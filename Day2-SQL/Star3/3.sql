SELECT  first_name,titles.title,employees.hire_date from employees inner join titles on employees.emp_no=titles.emp_no where titles.title='Assistant Engineer' order by hire_date limit 10 ;
SELECT  first_name,titles.title,employees.hire_date from employees inner join titles on employees.emp_no=titles.emp_no where titles.title='Senior Engineer' order by hire_date limit 10,10;
