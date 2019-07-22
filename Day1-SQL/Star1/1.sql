CREATE DATABASE ITC;
USE ITC;
CREATE TABLE user_table(
UseId INT,
FirstName VARCHAR(30),
LastName VARCHAR(30),
Gender VARCHAR(1),
Age INT,
Address VARCHAR(50),
City VARCHAR(50),
Country VARCHAR(20)
);

INSERT INTO user_table values(123,"Moshe","Cohen","M",20,"Dizengof","Tel aviv","Israel");

