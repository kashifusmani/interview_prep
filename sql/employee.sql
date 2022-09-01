-- https://www.psce.com/en/blog/2012/05/15/mysql-mistakes-do-you-use-group-by-correctly/
create table employee (
   emp_id int primary key,
   emp_name varchar(100),
   dept_id int references department(dept_id),
   salary int
);

create table department (
  dept_id int primary key,
  dept_name varchar(10)
);

insert into department values (1, "computer");
insert into department values (2, "networking");
insert into department values (3, "infra");

insert into employee values (1, "A", 1, 100);
insert into employee values (2, "B", 2, 200);
insert into employee values (3, "C", 3, 300);
insert into employee values (4, "D", 1, 200);
insert into employee values (5, "E", 2, 300);
insert into employee values (6, "F", 3, 100);
insert into employee values (7, "G", 1, 300);
insert into employee values (8, "H", 2, 100);
insert into employee values (9, "I", 3, 200);

--return employee record with highest salary
select * from employee where salary = (select max(salary) from employee);

--return second highest salary in employee table(or select employee with second highest salary)
select max(salary) from employee where salary not in (select max(salary) from employee)
--OR
select * from employee where salary = (select max(salary) from employee where salary not in (select max(salary) from employee))

--A better way
select * from (
  select salary,
    @salary_rank := IF(@type=dept_id, @salary_rank+1, 1) as salary_rank,
    @type := dept_id
  from (
    select distinct(salary) from employee order by salary desc) x
    )  y
  join employee where employee.salary = y.salary and y.salary_rank = 2

--return employee with highest salary and employee’s department name
select d.dept_name, e.emp_id where e.salary = (select max(salary) from employee)

--return highest salary, employee_name, department_name for each department
select e.salary, e.employee_name, d.dept_name
from employee e inner join department d
on e.dept_id = d.dept_id
having select max(e.salary), e.emp_id, d.dept_id
  from employee e
  inner join department d
  on e.dept_id = d.dept_id
  group by d.dept_id;


--OR
select emp_id, emp_name, e.dept_id, e.salary, d.dept_name from employee e
join
(select max(salary) as salary, dept_id from employee group by dept_id) as X
join
department d
on
e.dept_id = X.dept_id and e.salary = X.salary and e.dept_id = d.dept_id

-- return employee details with second higest salary in each department

select * from (
    select emp_id, emp_name, dept_id, salary,
    @salary_rank := IF(@type=dept_id, @salary_rank+1, 1) as salary_rank,
    @type := dept_id
    from employee
    order by dept_id, salary desc
    ) as X
where X.salary_rank = 2