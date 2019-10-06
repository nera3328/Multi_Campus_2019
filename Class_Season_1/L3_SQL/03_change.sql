
-- insert into / alter table () add
-- delete / alter table () drop
-- update 


-- 데이터를 추가하고 싶다면?
select database();
select * from sample41;
insert into sample41 value (1,'abc','2014-01-25');
select * from sample41;

-- data 참조 : desc table_name
desc sample41;

-- 특정 열에만 값을 추가하고 싶다면?
insert into sample41(no, a) values(2, 'def');
select * from sample41;
-- 한번에 여러 행을 추가하고 싶다면?
insert into sample41(no, a) value (3, 'asc'),(4, 'h');
select * from sample41;

-- NOT NULL 제약
insert into sample41 values(5, null, null);
select * from sample41;

-- default 값이 null이 아닌 값으로 설정되어 있다면?//행추가  --default가 0으로 설정되어있기때문.
desc sample411;
select * from sample411;
insert into sample411(no) values (1);
select * from sample411;

-- default 값이 null이 아닌 값으로 설정되어 있다면?//열추가  --default가 0으로 설정되어있기때문.
select * from sample41;
alter table sample41 add c varchar(10);
select * from sample41;
alter table smaple41 add e int(10);
select * from smaple41;

-- data 삭제하기
select * from sample41;
delete from sample41;
select * from sample41;
show tables;