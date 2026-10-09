create database company_db;

use company_db;
create table Employees(EmpId int NOT NULL, FirstName varchar(10), LastName varchar(10), EmpAge int);
desc Employees;

insert into Employees values(1, 'Rita', 'Zade', 20);
insert into Employees values(2, 'Riya', 'Rao', 21);
select * from Employees;

create table Employee1(EmpId int NOT NULL, FirstName varchar(10), LastName varchar(10), Unique (EmpId));
desc Employees;

insert into Employee1 values(Null, 'Ravi', 'Kumar');
insert into Employee1 values(1, 'Ravi', 'Kumar');

insert into Employee1 values(1, 'Ravi', 'Kumar');
insert into Employee1 values(2, 'Ravi', 'Kumar');

select * from Employee1;
desc Employee1;

create table Employee3(EmpId int NOT NULL, FirstName varchar(10), LastName varchar(10), EmpAge int, Check(EmpAge>20));
select * from Employee3;
desc Employee3;

insert into Employee3 values(1, 'Geeta', 'Kumari', 15);
insert into Employee3 values(1, 'Geeta', 'Kumari', 22);

alter table Employee3 add column Salary int;
alter table Employee3 add check (salary >= 5000);
update Employee3 set Salary=5000;

insert into Employee3 values(4, 'Nupur', 'Sharma', 25, 6000);

create table Employee7(EmpId int Primary Key, FirstName varchar(10), LastName varchar(10), EmpAge int);
insert into Employee7 values(NULL, 'Geeta', 'Kumari', 20);
alter table Employee7 add column Salary int;
alter table Employee7 add constraint chk_EmpAge_Salary check (EmpAge>20 AND Salary >= 5000);
desc Employee7;

select * from Employee7;

alter table Employee7 drop check Salary;

show create table Employee7;
alter table Employee7 drop check chk_EmpAge_Salary;
insert into Employee7 values(5, 'Anushka', 'Naik', 10, 1000);

create table Employee4(EmpId int NOT NULL, FirstName varchar(10), LastName varchar(10), EmpAge int);

use company_db;

create table Employee2(EmpId int Primary Key, FirstName varchar(10), LastName varchar(10), EmpAge int, Salary int);
alter table Employee2 add constraint chk_EmpAge_Salary check (EmpAge>20 AND Salary >= 5000);
desc Employee2;

insert into Employee2 values(1, 'Ram', 'Kumar', 22, 6000);
select * from Employee2;

show create table Employee2;

alter table Employee2 drop check chk_EmpAge_Salary;
alter table Employee2 add check (Salary >= 5000);
alter table Employee2 drop check employee2_chk_1;

-- the create index statement is used to create indexes in tables.
-- index are used to retrieve data from the database more quickly than otherwise

create Index Demoindex on Employee2(FirstName);
show indexes from Employee2; 

create Index Demoindex2 on Employee2(FirstName, LastName);

drop index Demoindex on Employee2;
drop index Demoindex2 on Employee2;



















