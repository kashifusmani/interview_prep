create table cities (
  city_code integer primary key,
  city_name varchar(20)
);

create table revenue (
  city_code integer,
  revenue integer
);

insert into cities (city_code, city_name) values (1, 'New York'), (2 , 'London'), (3, 'Paris');

insert into revenue (city_code, revenue) values (1,10), (2, 5), (2, 10), (3, 15);

select city_name, revenue from cities join
    (
        select cities.city_code,  floor(avg(revenue)) as revenue
        from cities join revenue on
        cities.city_code = revenue.city_code
        group by cities.city_code
    ) as x
on cities.city_code = x.city_code
