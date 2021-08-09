-- write your code in PostgreSQL 9.4
select distinct name
from (select name, year,
             lag(year, 2) over (partition by name order by min(year)) as last_two_years
      from participation
      group by name, year
     ) participation
where last_two_years = year - 2
order by name;
