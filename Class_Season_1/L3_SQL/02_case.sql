show database;
use sample;
show tables;
select * from sample21;
select no, name from sample21
where no=2;
select * from sample21;
select *from sample 37;
select a,
	case 
		when a is null
		then 0
	else a
end 'check_null' 
from 
	sample 37;
select a, 
	case 
		when a = 1 
			then '남자'
		when a= 2 
			then '여자'
		else '미지정'
	end 'decode' from sample37;
    ------사실 아래 함수로 그냥 실행 됨
    select coalesce(a) from sample37;g
select * from sample37;
delete from sample37 where a is null;
select * from sample37;

-- 열 삭제
alter table sample411 drop d;
select * from sampleadd 'c' varchar(10)411;

-- data 수정하기
select * from sample411;

-- 여러 열 추가
select * from sample41;
alter table sample41 add (f int(10), g int(10));
select *from sample41;

-- 여러 열 삭제
alter table sample51 drop (f,g);
select * from sample51;
desc sample51;
insert into sample51 values(1,'a','2019-06-05')
,(2,2,'x','2019-06-12');

-- UPDATE 문
update sample51 set name='z' where name is null;
select * from sample51;

update sample51 set name ='E', quantity=0 where no=5;
desc sample51;
select * from sample51;

-- no =+1, quantity = no(변경 후) 
-- ----> UPDATE는 SET의 순서대로 수행한다. (no랑 quantity순서 바꾸면 다름!)
update sample51 set no=no+1, quantity=no;
select *from sample51;

Update sample51 set quantity =0 where quantity <=4;
select * from sample51;
update sample51 set name='B' where name != 'A';
select * from sample51;

update sample51 set name=replace(name,'B','C');
select * from sample51;

-- Concat: 뒤에 문자를 붙임. 단, 문자 속성이 같아야 함.
update sample51 set quantity = concat(quantity, 0);
select * from sample51;

update sample51 set name= concat(name,'ZZ');
select * from sample51;


--  물리 삭제/// 논리삭제(칼럼을 참조만, 완전히 삭제하지 않고, 프론트에서만 지움 but 데이터가 늘어남/용량제한)
select * from sample51;
#dlt_flag
alter table sample51 add dlt_flag int(10);
update sample51 set dlt_flag = 1 where quantity= 0;
select * from sample51;

