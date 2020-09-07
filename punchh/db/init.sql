create database if not exists punchh_test;
use punchh_test;

create table if not exists email_campaigns (
  id bigint not null primary key auto_increment,
  business_id int not null,
  campaign_date date not null,
  email varchar(100) not null,
  event varchar(20) not null,
  campaign_name varchar(100) not null,
  sg_event_id varchar(100) not null,
  sg_message_id varchar(100) not null,
  timestamp bigint not null
)