use employees;
show tables;
select year(hire_date),count(*) from employees group by year(hire_date) order by year(hire_date);
select month(hire_date),count(*) from employees group by month(hire_date) order by month(hire_date);
select count(emp_no),dept_no,year(from_date) from dept_emp group by dept_no;
select emp_no,avg(salary) from salaries group  by emp_no;
select count(distinct(title)) from titles;
select title,count(*) from titles  group by title;
select emp_no,sum(salary) from salaries group  by emp_no;
select emp_no,   count(dept_no) from  dept_emp  group by emp_no order by count(dept_no) desc limit 1;
select gender,count(*) from employees group by gender;
select * from employees order by birth_date desc limit 10

