
-- count / sum / avg / min / max
-- group by에 의한 집계 / having


select database();
select * from sample54;
desc sample54;

-- count
select count(*) from sample54;
-- count로 테이블의 row 개수 계산가능
select *from sample54;
-- 특정 조건을 충족하는 row개수를 알고싶다면?
-- a < 100인 개수
select count(*) from sample54 where a<100;

insert into sample54(no) values(5);
select * from sample54;
select count(a) from sample54;  --  null은 count에서 제외

select * from sample51;
-- 중복 제거
select distinct name from sample51;

--  name의 고유값 개수를 count 하고 싶다면?
select count(distinct name) from sample51;

-- sum(합계)
select * from sample51;
select sum(quantity) from sample51;
select sum(dlt_flag) from sample51;
select sum(name) from sample51;   -- 문자열은 안나와여

-- avg(평균)
select avg(quantity) from sample51;
select avg(quantity)= sum(quantity) / count(qunantity) from sample51; 

-- min, max( 최소, 최대)
select min(no), max(no), min(name), max(name) from sample51;

insert into sample54 valuees <100 where

-- group by : 특정 열을 기준으로 집계츨 하고자 할 때
select * from sample51;
select name, avg(quantity) from sample51 group by name;

-- group by로 집계를 낸 후에 특정 조건을 충족하는 것만 select 하고 싶다면
select name, avg(quantity) from sample51 group by name having avg(quantity)>100;

select * from sample51;

select min(no), sum(dlt_flag) from sample51 group by name;

select min(no), sum(dlt_flag) from sample51 order by name decs;