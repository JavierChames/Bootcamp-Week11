CREATE DATABASE bootcamp_2019;
use bootcamp_2019;
CREATE TABLE student(id int unique not null AUTO_INCREMENT,firstName varchar(30) not null,lastName varchar(30)not null,course varchar(30),start_study_year varchar(4),end_study_year varchar(4),primary key (id));


CREATE TABLE cohort(id int unique not null AUTO_INCREMENT ,cohort_year varchar(4),primary key (id));

insert into student (firstName,lastName,course,start_study_year,end_study_year) values ("michal","cohen","Spanish","1995","1995");
insert into student (firstName,lastName,course,start_study_year,end_study_year) values ("eli","mama","math","1992","1992");
insert into student (firstName,lastName,course,start_study_year,end_study_year) values ("oshe","levi","spanish","2002","2002");

