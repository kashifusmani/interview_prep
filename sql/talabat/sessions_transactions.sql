
create table sessions_transaction (
  session_id integer primary key,
  transaction_id integer,
  vertical varchar(20)
);



insert into sessions_transaction (session_id, transaction_id, vertical) values
(1, null, 'Grocery'),
(2 , 1 , 'Grocery'),
(3, 2, 'Grocery'),
(4, null, 'Food'),
(5 , 3 , 'Food'),
(6, 4, 'Takeout'),
(7 , 5 , 'Takeout'),
(8, 6, 'Takeout'),
(9, null, 'Takeout')



●	Improving the session conversion rates from the vertical pages
= issued number of session order vs number of visits
Calculate session conversion rates


with
  t1 as (select count(session_id) as total, vertical from sessions_transaction group by vertical),
  t2 as ( select count(transaction_id) as totalTransactions, vertical from sessions_transaction
    group by vertical )
select t2.totalTransactions / t1.total, t2.vertical from t1 join t2 on t1.vertical= t2.vertical



●	Improving the click through rates on the organic list
of our food vertical=number of session with clicks on vertical page against number of sessions

create table sessions (
    session_id integer primary key,
    click_info varchar(20),
    vertical varchar(20)
);


insert into sessions (session_id, click_info, vertical) values
(1, null, 'Grocery'),
(2 , '1' , 'Grocery'),
(3, '2', 'Grocery'),
(4, null, 'Food'),
(5 , '3' , 'Food'),
(6, '4', 'Takeout'),
(7 , '5' , 'Takeout'),
(8, '6', 'Takeout'),
(9, null, 'Takeout')


with
  t1 as (select count(session_id) as total, vertical from sessions group by vertical),
  t2 as ( select count(click_info) as totalClicks, vertical from sessions group by vertical )
select t2.totalClicks / t1.total, t2.vertical from t1 join t2 on t1.vertical= t2.vertical
