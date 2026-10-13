-- 1. Create database named CompanyDB[cite: 1]
CREATE DATABASE CompanyDB;
USE CompanyDB;

-- 2. Create a table Employees with the following columns: EmpID (Integer, Primary Key), EmpName, Salary, and JoinDate.

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Salary DECIMAL(10, 2),
    JoinDate DATE
);

-- 3. Create a table Departments with the following columns: DeptID (Integer, Primary Key) and DeptName.
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

-- 4.Add a column Email of type VARCHAR(100) to the Employees table.
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);
DESC Employees;

-- 5.Add a column dept_location of type VARCHAR(100) to the Departments table.
ALTER TABLE Departments
ADD COLUMN dept_location VARCHAR(100);

-- 6.Add a Phone column to the Employees table and apply a NOT NULL constraint to it.
ALTER TABLE Employees
ADD COLUMN Phone VARCHAR(20);

ALTER TABLE Employees
MODIFY COLUMN Phone VARCHAR(20) NOT NULL;

-- 7.Change the size of the EmpName column from VARCHAR(50) to VARCHAR(100).
ALTER TABLE Employees
MODIFY COLUMN EmpName VARCHAR(100);

-- 8. Drop the primary key constraint from the Departments table.
ALTER TABLE Departments
DROP PRIMARY KEY;

-- 9. Create a foreign key constraint between the Employees and Departments tables using the DeptID column.
ALTER TABLE Departments
ADD PRIMARY KEY (DeptID);

ALTER TABLE Employees
ADD COLUMN DeptID INT,
ADD CONSTRAINT FK_Emp_Dept
FOREIGN KEY (DeptID)
REFERENCES Departments(DeptID);

-- 10. Rename the column EmpName to EmployeeName in the Employees table.
ALTER TABLE Employees
RENAME COLUMN EmpName TO EmployeeName;

-- 11. Apply a CHECK constraint on the Age and Salary columns so that age must be at least 18 and salary must be greater than zero.
ALTER TABLE Employees
ADD COLUMN Age INT;

ALTER TABLE Employees
ADD CONSTRAINT CHK_Age_Salary
CHECK (Age >= 18 AND Salary > 0);

-- 12. Remove the Phone column
ALTER TABLE Employees
DROP COLUMN Phone;

-- 13. Rename Employees to EmployeeDetails
RENAME TABLE Employees TO EmployeeDetails;

-- 14. Drop the CHECK constraint
ALTER TABLE EmployeeDetails
DROP CHECK CHK_Age_Salary;

ALTER TABLE EmployeeDetails
DROP FOREIGN KEY FK_Emp_Dept;

-- 15. Delete the Departments table permanently
DROP TABLE Departments;

-- 16. Drop the database
DROP DATABASE CompanyDB;



