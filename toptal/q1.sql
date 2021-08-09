SELECT
      test_groups.name,
      case when all_test_cases is null then 0 else all_test_cases end,
      case when passed_test_cases is null then 0 else passed_test_cases end,
      case when passed_test_cases is null then 0 else (X.passed_test_cases * test_value) end as total_value
from test_groups left join

(SELECT
  group_name as name,
  count(*) as all_test_cases,
  sum(case when status='OK' then 1 else 0 end) as passed_test_cases
 from test_cases group by group_name
 ) as X
on test_groups.name = X.name
order by total_value desc, name


create table test_groups (
      name varchar(40) not null,
      test_value integer not null,
      unique(name)
  );

 create table test_cases (
      id integer not null,
      group_name varchar(40) not null,
      status varchar(5) not null,
      unique(id)
  );

insert into test_groups (name, test_value) values
('performance', 15), ('corner cases', 10), ('numerical stability', 20), ('memory usage', 10);

insert into test_cases (id, group_name, status) values
(13, 'memory usage'        ,'OK'),
(14,  'numerical stability', 'OK'),
(  15,  'memory usage',        'ERROR'),
(  16,  'numerical stability', 'OK'),
(  17,  'numerical stability', 'OK'),
(  18,  'performance',         'ERROR'),
(  19,  'performance',         'ERROR'),
(  20,  'memory usage',        'OK'),
(  21,  'numerical stability', 'OK')