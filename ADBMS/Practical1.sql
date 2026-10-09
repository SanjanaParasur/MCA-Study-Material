Create database CompanyDB;
use CompanyDB;
Create table Employees(EmpId int, EmpName varchar(10), Salary decimal(10,2) , JoinDate date);
Create table Departments(DeptId int , deptName varchar(10));

alter table Employees add Email varchar(20);
alter table Departments add dept_loation varchar(10);
alter table Employees add Phone varchar(20);

alter table Employees modify Phone varchar(20) not null;

alter table Employees add primary key(EmpId);

alter table Departments add dept_loation varchar(10);

alter table Departments add primary key(DeptId);

alter table Employees modify EmpName varchar(20);

alter table Employees add DeptId int;
 alter table Employees add constraint fk_employee_department foreign key (DeptId) references Departments(DeptId);
 alter table Employees drop foreign key fk_employee_department;

alter table Departments drop primary key;

alter table Employees rename column EmpName to EmployeeName;
alter table Employees drop column Phone;

rename table Employees to EmployeeDetails;
drop table Departments;
desc EmployeeDetails;


 
 
 








