--
A table contains information about salaries and who is the manager of each employee.



Create a query that will return the second highest salary in the department.Departments are defined by ManagerId.



The report can contain manager information salary in case a manager is not the highest paid employee in the department.



Input data:

+----+------------------+--------------+-----------+

| ID | Name             | AnnualSalary | ManagerId |

+----+------------------+--------------+-----------+

| 1  | Lisa Smith       | 150000       | NULL      |

| 2  | Dan Bradley      | 110000       | 1         |

| 3  | Oliver Queen     | 180000       | 1         |

| 4  | Dave Dakota      | 100000       | 1         |

| 5  | Steve Carr       | 200000       | NULL      |

| 6  | Alice Johnson    | 205000       | 5         |

| 7  | Damian Luther    | 100000       | 5         |

| 8  | Avery Montgomery | 210000       | 5         |

| 9  | Mark Spencer     | 140000       | 5         |

| 10 | Melanie Thorthon | 200000       | NULL      |

| 11 | Dana Parker      | 100000       | 10        |

| 12 | Antonio Maker    | 120000       | 10        |

| 13 | Lucille Alvarez  | 140000       | 10        |

+----+------------------+--------------+-----------+



The expected output:

+----+-----------------+--------------+-----------+

| ID | Name            | AnnualSalary | ManagerId |

+----+-----------------+--------------+-----------+

| 1  | Lisa Smith      | 150000       | NULL      |

| 6  | Alice Johnson   | 205000       | 5         |

|13  | Lucille Alvarez | 140000       | 10        |

+----+-----------------+--------------+-----------+

create table departments (
      id integer not null,
      name varchar(40) not null,
      annualsalary integer not null,
      managerid integer
  );



insert into departments (id, name, annualsalary, managerid) values
(1, 'Lisa Smith', 150000, NULL),
(2, 'Dan Bradley', 110000, 1),
(3, 'Oliver Queen', 180000, 1),
(4, 'Dave Dakota', 100000, 1),
(5, 'Steve Carr ', 150000, NULL),
(6, 'Alice Johnson', 205000, 5),
(7, 'Damian Luther', 100000, 5),
(8, 'Avery Montgomery', 210000, 5),
(9, 'Mark Spencer', 140000, 5),
(10, 'Melanie Thorthon', 200000, NULL),
(11, 'Dana Parker', 100000, 10),
(12, 'Antonio Maker', 120000, 10),
(13, 'Lucille Alvarez', 140000, 10)


select ID, Name, AnnualSalary, ManagerId from
(
    select ID, Name, AnnualSalary, ManagerId,
           @salary_rank := if(@current_dept = departmentid, @salary_rank+1, 1) as salary_rank,
           @current_dept := departmentid
    from (
        select ID, Name, AnnualSalary, ManagerId, case when managerid is Null then id else  managerid end departmentid from departments
    ) Y order by departmentid, AnnualSalary desc)
X where salary_rank = 2
