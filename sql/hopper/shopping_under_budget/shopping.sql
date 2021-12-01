create table customers (
  id integer primary key,
  name varchar(20),
  budget integer
);


insert into customers (id, name, budget) values
(1, 'Kashif', 50),
(2 , 'Usmani' , 100);


create table products (
  code integer primary key,
  item varchar(20),
  price integer
);


insert into products (code, item, price) values
(1, 'Phone1', 10),
(2, 'Phone2', 20),
(3, 'Phone3', 30),
(4, 'Phone4', 40),
(5, 'Phone5', 50),
(6, 'Phone6', 60);

--STEP 1: Organize products in increasing order of prices

with cte as (
        select * , row_number() over(order by price asc) as rn from products
    ) select * from cte

+------+--------+-------+----+
| code | item   | price | rn |
+------+--------+-------+----+
|    1 | Phone1 |    10 |  1 |
|    2 | Phone2 |    20 |  2 |
|    3 | Phone3 |    30 |  3 |
|    4 | Phone4 |    40 |  4 |
|    5 | Phone5 |    50 |  5 |
|    6 | Phone6 |    60 |  6 |
+------+--------+-------+----+


--Step 2: Calculate total number of items that can be bought, starting with the cheapest item

select sum(X.price) as price, group_concat(code) as item_codes, X.rn as total_items from (
    with cte as (
        select * , row_number() over(order by price asc) as rn from products
    )
    select A.code, A.item, A.price, B.rn from cte as A join cte as B on A.rn <= B.rn
) as X group by X.rn order by price asc;

--Gives
+-------+-------------+-------------+
| price | item_codes  | total_items |
+-------+-------------+-------------+
|    10 | 1           |           1 |
|    30 | 1,2         |           2 |
|    60 | 1,2,3       |           3 |
|   100 | 1,2,3,4     |           4 |
|   150 | 1,2,3,4,5   |           5 |
|   210 | 1,2,3,4,5,6 |           6 |
+-------+-------------+-------------+
--

-- Step 3: Now that we know how many items can be bought for a given total amount, we will iterate over each row of
-- Customers and calculate how many each can buy
with cte_3 as (
    with recursive cte_2 (budget, id) as (select budget, id from customers),
        sub as
                 (
                     select sum(X.price) as price, group_concat(code) as item_codes, X.rn as total_items from (
                         with cte as (
                             select * , row_number() over(order by price asc) as rn from products
                         )
                         select A.code, A.item, A.price, B.rn from cte as A join cte as B on A.rn <= B.rn
                     ) as X group by X.rn order by price asc
                 )

    select * from sub join cte_2 where price <=budget
)
select * from cte_3;

+-------+------------+-------------+--------+----+
| price | item_codes | total_items | budget | id |
+-------+------------+-------------+--------+----+
|    10 | 1          |           1 |    100 |  2 |
|    10 | 1          |           1 |     50 |  1 |
|    30 | 1,2        |           2 |    100 |  2 |
|    30 | 1,2        |           2 |     50 |  1 |
|    60 | 1,2,3      |           3 |    100 |  2 |
|   100 | 1,2,3,4    |           4 |    100 |  2 |
+-------+------------+-------------+--------+----+

select max(total_items) as total_items, budget, id as customer_id from cte_3 group by budget, id;

--Gives
+-------------+--------+-------------+
| total_items | budget | customer_id |
+-------------+--------+-------------+
|           4 |    100 |           2 |
|           2 |     50 |           1 |
+-------------+--------+-------------+