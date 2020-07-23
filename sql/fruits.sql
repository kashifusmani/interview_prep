create table fruits
(
type varchar(10),
variety varchar(10),
price int
);

insert into fruits values ("apple", "gala", 2);
insert into fruits values ("apple", "fuji", 1);
insert into fruits values ("apple", "limbertwig", 3);
insert into fruits values ("orange", "valencia", 3);
insert into fruits values ("orange", "navel", 9);
insert into fruits values ("pear", "bradford", 6);
insert into fruits values ("pear", "bradford", 2);
insert into fruits values ("cherry", "bing", 2);
insert into fruits values ("cherry", "chelan", 6);


--Get Most expensive from each category

select * from (
	select type, variety, price,
	@price_rank := IF(@current_type = type, @price_rank+1,1) as price_rank,
	@current_type := type
 from fruits  order by type, price desc) ranked where price_rank <=1

--Get cheapest from each category

select type, variety, price
from fruits
where (
   select count(*) from fruits as f
   where f.type = fruits.type and f.price <= fruits.price
) <= 2;


--Or, more efficient

(select * from fruits where type = 'apple' order by price limit 2)
union all
(select * from fruits where type = 'orange' order by price limit 2)
union all
(select * from fruits where type = 'pear' order by price limit 2)
union all
(select * from fruits where type = 'cherry' order by price limit 2)

