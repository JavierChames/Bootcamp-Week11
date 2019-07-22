use employees;
select gender,count(*) from employees group by gender;
select count(distinct(title)) from titles;
SELECT  first_name,titles.title,employees.hire_date from employees inner join titles on employees.emp_no=employees.emp_no where year(hire_date)='1993';
SELECT  first_name,titles.title,employees.hire_date from employees inner join titles on employees.emp_no=titles.emp_no where titles.title='Staff';
SELECT  first_name,last_name,salaries.salary,titles.title from employees inner join salaries on employees.emp_no=salaries.emp_no inner join titles on employees.emp_no=titles.emp_no where titles.title='Staff' group by first_name order by salary desc limit 10;
select t.title, avg(s.salary) as "avg salary" from titles as t inner join salaries as s on t.emp_no = s.emp_no group by title;
