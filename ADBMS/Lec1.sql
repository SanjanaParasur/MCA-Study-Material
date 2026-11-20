Create database Institute;
use Institute;
Create table Staff(staff_id int, first_name varchar(10), last_name varchar(10),DOB date, dept_id int);
Create table Department(dept_id int, dept_name varchar(10), dept_location varchar(15));

desc Staff;
desc Department;

alter table Staff add (location varchar(20), joining_year date);
alter table Staff add (Age int,Contact_no int);
alter table Staff modify last_name text;

alter table Staff drop contact_no;
alter table Staff add primary key(staff_id);
alter table Department add primary key(dept_id);

desc Staff;
desc Department;

-- Syntax: Alter table tablename add foreign key (columnname) references 2nd tablename (column);

alter table Staff add foreign key(dept_id) references Department(dept_id);

desc Staff;

Alter table Staff rename Staff1;
desc Staff1;
rename table Staff1 to Staff;

alter table Staff rename column first_name to FirstName;

Drop table Department;
Drop table Staff;
Drop database Institute;