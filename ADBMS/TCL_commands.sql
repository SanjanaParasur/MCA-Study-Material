create database TCL;
use TCL;

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_name VARCHAR(100),
status varchar(50));
desc orders;

-- Start the Transaction--
set autocommit=0;

begin;
insert into orders values (104, 'Geet', 'Pending'); 
insert into orders values (102, 'Bob', 'Pending');
-- truncate table orders;
select * from orders;
rollback;
commit; /*we are not able to rollback after commit*/

insert into orders values (103, 'Raj', 'Pending'); 
insert into orders values (101, 'Rahul', 'Pending');
rollback; 
select * from orders;

update orders set Customer_Name='Meena' where order_id=103;
rollback;

-- Step 1: Insert a few orders
insert into orders values (105, 'Om', 'Pending');
insert into orders values (106, 'Sahil', 'Pending');
savepoint sp1;
select * from orders;

-- Step 2:Update one order
Update orders set Customer_Name='Alice' where order_id=106;
rollback to savepoint sp1; /* will undo the changes*/

-- Step 3:Delete another order
delete from orders where order_id = 102;
savepoint sp3;

-- We want to undo the delete but keep the update
rollback to savepoint sp1;
select * from orders;
rollback;


