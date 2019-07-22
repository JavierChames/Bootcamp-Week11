CREATE DATABASE programs;
USE programs;
CREATE TABLE Participant(id int unique not null ,firstName varchar(30) not null,lastName varchar(30)not null,country varchar(30),gender varchar(1) not null,levelOfEnglish int,israel_citizen boolean,primary key (id));
CREATE TABLE Payment(id int unique not null ,participantId int not null,sum int,date DATE,paymentMethod  ENUM('limited to cash','paypal') ,authorizationCode varchar(10),primary key(id),foreign key (id) references Participant(id) on update cascade on delete restrict);

INSERT INTO Participant values(1,"Moshe","Cohen","USA","M",7,TRUE);
INSERT INTO Participant values(2,"MICHAL","LEVI","SPAIN","F",10,false);

INSERT INTO payment values(1,1,10,'1990-01-02',"paypal",7);
INSERT INTO payment values(2,2,20,'1980-01-01',"limited to cash",10);

delete from Participant where id='1';
-- 14:34:29	delete from Participant where id='1'	Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`programs`.`payment`, CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`id`) REFERENCES `participant` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE)	0.062 sec


