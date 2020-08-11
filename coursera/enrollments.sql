create table enrollments (
  student_id integer,
  course_id integer,
  grade integer
);

insert into enrollments values (1, 4, 50);
insert into enrollments values (1, 2, 49);
insert into enrollments values (1, 5, 50);

insert into enrollments values (2, 1, 48);
insert into enrollments values (2, 2, 48);
insert into enrollments values (2, 3, 48);

insert into enrollments values (3, 2, 48);
insert into enrollments values (3, 3, 50);

select enrollments.student_id,
      min(course_id) as course_id,
      enrollments.grade from enrollments
        join (
            select student_id,
            max(grade) as grade
            from enrollments
            group by student_id )
        as X
      on enrollments.student_id = X.student_id
      and enrollments.grade = X.grade
      group by enrollments.student_id, enrollments.grade
      order by enrollments.student_id asc

----

create table enrollments
(
user_id int,
session_id int,
is_sigtrack char
);

insert into enrollments values (1, 1, 'Y');
insert into enrollments values (1, 1, 'Y');
insert into enrollments values (1, 1, 'Y');
insert into enrollments values (1, 1, 'N');
insert into enrollments values (1, 1, 'N');
insert into enrollments values (1, 1, 'Y');

select count(*) as total_enrollments, sum(if(e.is_sigtrack='Y', 1, 0)) as paid_enrollments from enrollments e
