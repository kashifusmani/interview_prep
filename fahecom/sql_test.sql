Game Play Analysis
Table: Activity
+--------------+---------+
| Column Name | Type |
+--------------+---------+
| player_id | int |
| device_id | int |
| event_date | date |
| games_played | int |
+--------------+---------+
(player_id, event_date) is the primary key of this table. This table shows the activity of players of some game. Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.
Write an SQL query that reports the first login date for each player. The query result format is in the following example: Activity table:

+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played | +-----------+-----------+------------+--------------+
 | 1 | 2 | 2016-03-01 | 5 |
 | 1 | 2 | 2016-05-02 | 6 |
 | 2 | 3 | 2017-06-25 | 1 |
 | 3 | 1 | 2016-03-02 | 0 |
 | 3 | 4 | 2018-07-03 | 5 |
 +-----------+-----------+------------+--------------+

Result table:
+-----------+-------------+
| player_id | first_login |
| 1              | 2016-03-01 |
| 2              | 2017-06-25 |
| 3              | 2016-03-02 |
+-----------+-------------+


Write SQL query to calculate MoM Percent Change for MAU?
Oftentimes it's useful to know how much a key metric, such as monthly active users, changes between months. Consider below logins table with sample data
user_id
login_date
1
2022-07-01
3
2022-07-02
50
2022-01-05
1
2022-03-05
3
2022-02-07
5
2022-05-10
1
2022-04-14

Task
Find the month-over-month percentage change for monthly active users (MAU)

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
+------+----------+-----------+----------+
|Id |Name |Department |ManagerId |
+------+----------+-----------+----------+
|101 |John |A |null |
|102 |Dan |A |101 |
|103 |James |A |101 |
 |104 |Amy |A |101 |
|105 |Anne |A |101 |
|106 |Ron |B |101 |
+------+----------+-----------+----------+


Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:
 +-------+
| Name |
+-------+
 | John |
+-------+
Note: No one would report to himself.

