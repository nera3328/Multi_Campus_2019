-- count / sum / avg / min / max
-- group by 에 의한 집계 / having

select database();
select * from sample54;
desc sample54;

-- count 
select count(*) from sample54;
-- count로 테이블의 row 개수 계산 가능
select * from sample54;
-- 특정 조건을 충족하는 row 개수를 알고 싶다면?
-- a < 100 인 개수
select count(*) from sample54 where a < 100;


insert into sample54(no) values (5);
select * from sample54; 
select count(a) from sample54; -- null은 count에서 제외

select * from sample51;
-- 중복 제거
select distinct name from sample51;

-- name의 고유값의 개수를 count 하고 싶다면?
select count(distinct name) from sample51;

-- sum (합계)
select * from sample51;
select sum(quantity) from sample51;
select sum(dlt_flag) from sample51;
select sum(name) from sample51;

-- avg (평균)
SELECT 
    AVG(quantity), SUM(quantity) / COUNT(quantity)
FROM
    sample51;
    
-- min, max (최소, 최대)
SELECT 
    MIN(no), MAX(no), MIN(name), MAX(name)
FROM
    sample51;

-- group by : 특정 열을 기준으로 집계를 하고자할때
select * from sample51;
SELECT 
    name, AVG(quantity)
FROM
    sample51
GROUP BY name;

-- group by로 집계를 낸 후에 
-- 특정 조건을 충족하는 것만 select하고 싶다면
SELECT 
    name, AVG(quantity)
FROM
    sample51
GROUP BY name
HAVING AVG(quantity) > 1000;

select * from sample51;

SELECT 
    name, MIN(no), SUM(quantity), AVG(dlt_flag)
FROM
    sample51
GROUP BY name
ORDER BY MIN(no) DESC;

