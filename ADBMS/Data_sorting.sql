create database user;
show databases;

use user;
create table customer (Custid int, custname varchar(15), City varchar(10), product varchar(15), Price int);

desc customer;

alter table customer add constraint primary key(Custid);
insert into customer values(1, 'Om', 'Pune', 'Mobile', '15000');
insert into customer values(2, 'Rucha', 'Nagpur', 'laptop', '40000');
insert into customer values(3, 'Raj', 'Mumbai', 'Mouse', '300');

select * from customer;
select custname, product from customer;
create table CloneTable as select * from customer;
select * from CloneTable;
drop table CloneTable;

/*Where Clause*/
select custname, city from customer;

select custname , city from customer where custid=1;

select custname, product, price from customer where price>15000;

select custname, product, price from customer where price<15000;

select * from customer where price>15000;

select * from customer where custid=1;

select * from customer where City='Nagpur';

/*Sorting data using Order by single column*/

select * from customer order by price;

select * from customer order by price desc;

select * from customer order by price asc;

select * from customer order by City asc;

/*Sorting data Order by multiple columns*/

select * from customer order by City, price;
select * from customer order by price, City;

select * from customer order by city desc, price asc;

/*Single row functions*/
/*Case conversion functions*/

select upper(Custname), lower(product) from customer where Custid<3; /*uppercase & lowercase function*/

alter table customer add column Lastname varchar(20);
update customer set Lastname = 'Sharma' where Custid=1;
update customer set Lastname = 'Verma' where Custid=2;
update customer set Lastname = 'Roy' where Custid=3;

select * from customer;

/*concat two columns*/
select concat(custname,lastname) from customer;
select concat(custname,' ',lastname) from customer;

/*concat column name change*/
select concat(custname,' ',lastname) as FullName from customer;

/*use of SUBSTR and INSTR function*/
select * from customer;
select substr(custname,1,0) from customer;
select substr(custname,1,1) from customer;
select substr(custname,0,1) from customer;
select substr(custname,2,1) from customer;/* start from second letter and return one letter*/
select substr(custname,1,3) from customer;/* start from first letter and return three letters*/

/*substring query*/
select instr(custname, 'a') as position from customer;


/* Date and time function*/
select now();
select now() as current_datetime;
 alter table customer add column date date;
 
 update customer set date="2024-02-28" where custid=1;
 update customer set date="2024-08-26" where custid=2;
 update customer set date="2024-10-02" where custid=3;
 
 /*Filtering data from user*/
 /* Where select distinct, and, or, not, in, between,like,limit,is null*/
 drop database organisation;
 create database organisation;
 use organisation;
 
 create table employee(Empid int not null primary key, First_name varchar(15), Last_name varchar(20), Gender char, Role varchar(15), dept varchar(15), Manager_id varchar(10));
 desc employee;
 
 insert into employee values(1, 'John', 'Allen', 'M', 'TeamLeader', 'Retail', 'M11');
 insert into employee values(2, 'Kim', 'Hen', 'F', 'TeamLeader', 'Finance', 'M12');
 insert into employee values(3, 'Ravi', 'Kumar', 'M', 'Manager', 'Retail', 'M13');
 insert into employee values(4, 'Aruna', 'Patel', 'F', 'Manager', 'Finance', 'M14');
 insert into employee values(5, 'Kirti', 'Rai', 'F', 'President', 'HR', 'M15');
 
 SELECT * FROM employee;
select distinct Dept from employee order by Dept;
select distinct Role from employee order by Role;

select * from employee where role='President' and dept='HR';
select * from employee where role='President' and dept='Retail';

select * from employee where role='Manager' or role='Team Leader';

/* In operator: the in operator is used to determine if a value matches any othe value in a list. If the value equals any value in the list(value1, value2, value3,...), In operator returns 1 (true). */ 

select * from employee where role in ('President', 'Manager');
select * from employee where role in ('CEO', 'Manager');

/* Not In operator*/
select * from employee where role not in ('President', 'Manager');

/*BETWEEN Operator*/

alter table employee add column Exprience int;

select * from employee;

update employee set Exprience=8 where Empid=1;
update employee set Exprience=5 where Empid=2;
update employee set Exprience=10 where Empid=3;
update employee set Exprience=8 where Empid=4;
update employee set Exprience=15 where Empid=5;

select * from employee;
select * from employee where Exprience between 6 and 10;/*BETWEEN Operator*/
select * from employee where Exprience=2 or Exprience=10;

/*Like Operator*/

select * from employee where last_name like 'A%';
select * from employee where last_name like 's%';

/*Limit Operator*/
select * from employee;
select * from employee order by exprience limit 5;

/* Is Null Operator*/
insert into employee(Empid, First_Name, Last_Name, Gender, Role, Dept) values (8, 'Usha', 'Yadav', 'F', 'President', 'Finance');
select * from employee;
select * from employee where manager_id is null;

/*Is not null*/
select * from employee where manager_id is not null;















