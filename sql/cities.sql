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

select city_name, floor(avg(revenue)) from cities join revenue on
cities.city_code = revenue.city_code
group by cities.city_code

---

create table customer (
  id integer primary key,
  customer_name varchar(255),
  city_id int,
  customer_address varchar(255),
  contact_person varchar(255),
  email varchar(128),
  phone varchar(128)
);

create table product (
  id integer primary key,
  sku varchar(32),
  product_name varchar(128),
  product_description text,
  current_price decimal(8,2),
  quantity_in_stock integer
);

create table invoice(
  id integer primary key,
  invoice_number varchar(255),
  customer_id integer,
  user_account_id integer,
  total_price decimal(8, 2),
  time_issued varchar(255),
  time_due varchar(255),
  time_paid varchar(255),
  time_cancelled varchar(255),
  time_refunded varchar(255),
  FOREIGN KEY (customer_id) REFERENCES customer(id)
);

create table invoice_item(
  id integer primary key,
  invoice_id integer,
  product_id integer,
  quantity decimal(8, 2),
  price decimal(8,2),
  line_total_price decimal(8,2),
  FOREIGN KEY (invoice_id) REFERENCES invoice(id),
  FOREIGN KEY (product_id) REFERENCES product(id)
);



insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (1, 'Drogerie Wien', 1, 'Deckergasse 15A', 'Emil Steinbach', 'emil@drogeriewien.com', 094234234);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (2, 'Cosmetic Store', 4, 'Watling Street 347', 'Jeremy Corbyn', 'jeremy@c-store.org',093923923);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (3, 'Kosmeticstudio', 3, 'Rothenbaumchaussee 53', 'Willy Brandt', 'willy@kosmetikstudio.com', 0941562222);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (4, 'Neue Kosmetic', 1, 'Karlsplatz 2', NULL, 'info@neuekosmetic.com', 094109253);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (5, 'Bio Kosmetic', 2, 'Motzstrabe 23' ,'Clara Zetkin', 'clara@biokosmetic.org', 093825825);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (6, 'K-Wien', 1, 'Kartner Strabe 204', 'Maria Rauch-Kallat', 'maria@kwien.org', 093427002);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (7, 'Natural Cosmetics', 4, 'Clerkenwell Road 14B', 'Glenda Jackson', 'glena.j@natural-cosmetics.com', 093555123);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (8, 'Kosmetic Plus', 2, 'Unter den Linden 1', 'Angela Merkel', 'angela@k-plus.com', 094727727);
insert into customer (id, customer_name, city_id, customer_address, contact_person, email, phone) values (9, 'New Line Cosmetics', 4, 'Devonshire Street 92', 'Oliver Cromwell', 'oliver@nlc.org', 093202404);


insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (1, '330120', 'Game of Thrones- URBAN DECAY', 'Game of Thrones Eyeshadow Palette', 65, 122);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (2, '330121', 'Advanced Night Repair - ESTEE LAUDER', 'Advanced Night Repair Synchronized Recovery Complex II', 98, 51);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (3, '330122', 'Rose Deep Hydration - FRESH', 'Rose Deep Hydration Facial Toner', 45, 34);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (4, '330123', 'Pore-Perfecting Moisturizer - TATCHA', 'Pore-Perfecting Moisturized & Cleanser Due', 25, 393);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (5, '330124', 'Capture Youth - DIOR', 'Capture Youth Serum Collection', 95, 74);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (6, '330125', 'Slice of Glow - GLOW RECIPE', 'Slice of Glow Set', 45, 40);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (7, '330126', 'Healthy Skin - KIEHLS SINCE 1851', 'Healthy Skin Squad', 68, 154);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (8, '330127', 'Power Pair! - IT COSMETICS', 'IT is Your Skincare Power Pair! Best-Selling Moisturized & Eye Cream Duo', 80, 0);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (9, '330128', 'Dewy Skin Mist - TATCHA', 'Limited Edition Dewy Skin Mist Mini', 20, 281);
insert into product (id, sku, product_name, product_description, current_price, quantity_in_stock) values (10, '330129', 'Silk Pillowcase - SLIP', 'Silk Pillowcase Duo + Scrunchies Kit', 170, 0);


insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (1, 'in_251', 7, 4, 1436, '7/20/2019 3:05:07 PM', '7/27/2019 3:05:07 PM', '7/25/2019 9:24:12 AM', NULL, NULL);
insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (2, '8fba', 9, 2, 1000, '7/20/2019 3:07:11 PM', '7/27/2019 3:05:11 PM', '7/20/2019 3:10:32 PM', NULL, NULL);
insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (3, '3b66', 3, 2, 360, '7/20/2019 3:06:15 PM', '7/27/2019 3:06:15 PM', '7/31/2019 9:22:11 AM', NULL, NULL);
insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (4, 'dfe7', 5, 2, 1675, '7/20/2019 3:06:34 PM', '7/27/2019 3:06:34 PM', NULL, NULL, NULL);
insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (5, '2a24', 6, 2, 9500, '7/20/2019 3:06:42 PM', '7/27/2019 3:06:42 PM', NULL, '7/22/2019 11:17:02 AM', NULL);
insert into invoice (id, invoice_number, customer_id,user_account_id, total_price,  time_issued,  time_due,  time_paid ,  time_cancelled,  time_refunded) values (6, 'cbd3', 4, 2, 150, '7/20/2019 3:08:15 PM', '7/27/2019 3:08:15 PM', '7/27/2019 1:42:45 PM', NULL, '7/27/2019, 2:11:20 PM') ;


insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (1, 1, 1, 20, 65, 1300);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (2, 1, 7, 2, 68, 136);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (3, 1, 5, 10, 100, 1000);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (4, 3, 10, 2, 180, 360);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (5, 4, 1, 5, 65, 325);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (6, 4, 2, 10, 95, 950);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (7, 4, 5, 4, 100, 400);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (8, 5, 10, 100, 95, 9500);
insert into invoice_item (id, invoice_id,  product_id ,  quantity ,  price ,  line_total_price ) values (9, 6, 4, 6, 25, 150);


select
 IFNULL(customer_name, 'N/A') as customer_name,
 IFNULL(product_name, 'N/A') as product_name,
 IFNULL(quantity,0) as quantity from
    (
      select a.customer_name, d.product_name, c.quantity,
        a.id as customer_id, d.id as product_id, c.id as invoice_item_id from
      customer a
      left outer join invoice b on a.id=b.customer_id
      left outer join invoice_item c on b.id = c.invoice_id
      left outer join product d on c.product_id = d.id

      union

      select a.customer_name, d.product_name, c.quantity,
        a.id as customer_id, d.id as product_id, c.id as invoice_item_id from
      product d
      left outer join invoice_item c on d.id = c.product_id
      left outer join invoice b on b.id=c.invoice_id
      left outer join customer a on a.id = b.customer_id
    ) x
order by customer_id, product_id, invoice_item_id asc