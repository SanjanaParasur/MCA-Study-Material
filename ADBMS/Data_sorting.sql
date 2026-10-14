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













