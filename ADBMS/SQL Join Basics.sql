Drop database basicjoin;
create database Basicjoin;
use Basicjoin;
create table employee(employee_id int primary key, ename varchar(30));
insert into employee values(101,"Sanjana");
insert into employee values(102,"Tanaya");
insert into employee values(103,"Atharva");
insert into employee values(104,"Vansh");
insert into employee values(105,"Samrudhi");

create table projects(project_id int primary key, pname varchar(50), employee_id int, foreign key(employee_id) references employee(employee_id));
insert into projects(project_id, pname, employee_id) 
values (1, 'Project A', 101),
       (2, 'Project B', 102),
       (3, 'Project C', 101),
       (4, 'Project D', 103);
select * from projects;

insert into Projects values(5, 'Project E', 103); 
insert into Projects values(6, 'Project F', null); 


/* only matching records will display from employee and project table*/
select * from employee 
JOIN projects
 on employee.employee_id = projects.employee_id;
 
 select e.ename, p.pname from projects p
 inner join employee e ON e.employee_id = p.employee_id;
 
 select e.ename, p.pname from employee e
 left join projects p
 ON e.employee_id = p.employee_id;
 
  select e.ename, p.pname from projects p
 left join employee e 
 ON e.employee_id = p.employee_id;
 
  select e.ename, p.pname from employee e
 right join projects p 
 ON e.employee_id = p.employee_id;
 
 insert into projects(project_id, pname)
 values(8, 'Project I');
 
 insert into employee values(106,"Ayush");
insert into employee values(107,"Arnav");

select * from employee left join projects 
on employee.employee_id = projects.employee_id;
 
 
 select * from employee 
 left join projects
 on employee.employee_id = projects.employee_id
 union
 select * from employee
 right join projects
 on employee.employee_id = projects.employee_id;
 
 /* display employee name who has not assigned any project*/
 select employee.ename, projects.pname
 from employee
 left join projects
 on employee.employee_id = projects.employee_id
 where projects.employee_id is not null;
 
  select employee.ename, projects.pname
 from employee
 left join projects
 on employee.employee_id = projects.employee_id
 where projects.employee_id is null;