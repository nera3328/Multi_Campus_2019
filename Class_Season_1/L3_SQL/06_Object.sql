select database();
use sample;

-- 명령어 객체 객체명!          #타입 정하기(이름은 no, integer)
create table sample62(
no integer not null,     
a varchar(30),
b date);

desc sample62;
insert into sample62 values(1,'ardino','2019-06-13');
select * from sample62;

-- delete: 행을 탐색해서 삭제하기 때문에 시간이 좀 걸림 where을 써줘서 특정 행을 찾음, 안쓰면 다지워버림 
-- trumcate: delete보다 빠름!

truncate table sample62;
select * from sample62;

drop table sample62;
select * from sample62;

create table student_list(
no integer not null,   # (특정 고유값!)
name varchar(20)
);

select * from stydent_list;
alter table student_list add birth date;
-- birth 열의 속성을 varchar(10)으로 수정해보세여
-- birth 열의 이름을 date로 수정해 보세요

alter table student_list modify date varchar(10) not null;;
desc student_list;

alter table student_list modify birth varchar(10) not null;
desc student_list;

-- date 열을 다시 birth로 바꾸고, 속성은 date로 
alter table student_list change date date;

create index index_student on student_list(no);
select * from student_list;

insert into student_list values(1,'dino','2019-06-12'),(2,'inno','2019-06-13');

# EXPLAIN : 인덱스 확인alter
explain select * from student_list where no >1;

drop index index_student on student_list;
#index_student -> null
explain select * from student_list where no >1;

--  view
create view view_student as select * from student_list;

create view view_no_name as select no, name from student_list;

drop view view_no_name;

select * from student_list where no >1;

#이진탐색 p160
