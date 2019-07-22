use employees;
select dept_name from departments;
select * from employees where gender ="f" and first_name="Elvis";
select * from employees where last_name in('Merlo','Smith','Albin','Unno','Baba','Luft','Ozeri','Dalton','Peck');
select * from employees where year(hire_date) in('1995','1996') order by hire_date desc;
select * from employees where first_name like 'A%' and last_name like '%B';
select * from salaries order by salary desc limit 5;
select * from employees where hire_date > (select hire_date from employees where first_name='Jagoda' and last_name='Nannarelli');
