CREATE DATABASE bootcamp;
USE bootcamp;
CREATE TABLE students(
student_id INT,
FirstName VARCHAR(30),
LastName VARCHAR(30),
been_dismissed VARCHAR(1),
cohort INT
);
CREATE TABLE grades(
student_id INT,exam_id int,date_taken date,grade int);
INSERT INTO students values(123,"Moshe","Cohen","Y",20);
INSERT INTO students values(128,"bibi","Cohen","N",25);
INSERT INTO students values(125,"itzik","Cohen","Y",20);
update students set Firstname="miki" where cohort=20;
delete from students where FirstName like '%ib%'

