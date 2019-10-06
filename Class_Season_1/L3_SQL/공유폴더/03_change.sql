-- insert into / alter table () add
-- delete / alter table () drop
-- update 

-- 데이터를 추가하고 싶다면?
select database();
select * from sample41;
insert into sample41 values (1, 'abc', '2014-01-25');
select * from sample41;

-- data 참조 : desc table_name
desc sample41;

-- 특정 열에만 값을 추가하고 싶다면?
insert into sample41(no, a) values (2, 'def');
select * from sample41;

-- 한번에 여러 행을 추가하고 싶다면?
insert into sample41(no, a) values(3, 'g'), (4, 'h');
select * from sample41;

-- NOT NULL 제약
insert into sample41 values(NULL, NULL, NULL);
select * from sample41;

insert into sample41 values(5, NULL, NULL);
select * from sample41;

-- default 값이 null 이 아닌 값으로 설정되어있다면?
desc sample411;
select * from sample411;
insert into sample411(no) values (1);
select * from sample411;

-- 열 추가
select * from sample41;
alter table sample41 add c varchar(10); 
select * from sample41;

-- 원하는 위치에 넣기
alter table sample41 add d int(10) after no;
select * from sample41;

-- 맨 앞에 넣기
alter table sample41 add e int(10) first;
select * from sample41; 

-- 여러 열 추가
select * from sample41;
alter table sample41 add (f int(10), g int(10));
select * from sample41;



-- data 삭제하기
select * from sample41;
delete from sample41;
select * from sample41;

select * from sample37;
delete from sample37 where a is null;
select * from sample37;

-- 열 삭제
-- alter table sample37 drop a;
select * from sample411;
alter table sample411 drop d;
select * from sample411;

-- 여러 열 삭제
alter table sample41 drop c;
select * from sample41;
alter table sample41 drop c;

-- data 수정하기(update)
select * from sample51;
desc sample51;

update sample51 set name = 'Z' where name is null;
select * from sample51;
UPDATE sample51 
SET 
    name = 'E',
    quantity = 0
WHERE
    no = 5;
select * from sample51;

-- no = no + 1, quantity = no(변경 후)
update sample51 set no = no+1, quantity = no;
select * from sample51;

-- update는 set의 순서대로 수행한다.
update sample51 set quantity = no, no = no+1;
select * from sample51;

update sample51 set quantity = 0 where quantity <= 4;
select * from sample51;

update sample51 set name = 'B' where name <> 'A';
select * from sample51;

update sample51 set name = replace(name, 'B', 'C');
select * from sample51;
 
update sample51 set quantity = concat(quantity, 0);
select * from sample51;

update sample51 set name = concat(name, 'zzz');
select * from sample51;

-- 물리 삭제 vs 논리 삭제
select * from sample51;
#dlt_flag
alter table sample51 add dlt_flag int(10);
select * from sample51;
update sample51 set dlt_flag = 1 where quantity = 0;
select * from sample51;


