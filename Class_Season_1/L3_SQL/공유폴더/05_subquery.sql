

select * from sample54;

select min(a) from sample54;

SELECT 
    a
FROM
    sample54
WHERE
    no = (SELECT 
            MIN(no)
        FROM
            sample54);
            
# a > avg(a)일 때의 no를 뽑아줘.
SELECT 
    no
FROM
    sample54
WHERE
    a > (SELECT 
            AVG(a)
        FROM
            sample54);
            
SELECT 
    (SELECT 
            COUNT(*)
        FROM
            sample51) as len_s51,
    (SELECT 
            COUNT(*)
        FROM
            sample54) as len_s54;
            
select * from sample34;
# a값을 a의 최대값으로 업데이트하기
UPDATE sample54 
SET 
    a = (SELECT 
            MIN(price)
        FROM
            sample34);
select * from sample54;

SELECT 
    *
FROM
    (SELECT 
        price
    FROM
        sample34) price;
        
SELECT 
    *
FROM
    (SELECT 
        *
    FROM
        sample54
    ORDER BY no DESC) s54
WHERE
    no >= 4;
    
select * from sample541;
select * from sample54;
select * from sample51;

-- sample54의 길이와 sample51의 길이를 sample541의 a, b 열에 각각 추가해보세요.
insert into sample541 values ((select count(*) from sample54),
(select count(*) from sample51));

-- value 대신 select이용해서 insert 사용
insert into sample541 values (1, 2);
insert into sample541 select 1, 2;

select * from sample551; # 열 2개인지 확인
alter table sample551 drop b; # b열이 있을경우 삭제
insert into sample54 select * from sample551; 
insert into sample54 select * from sample541;
insert into sample54 select no, quantity from sample51;
select * from sample54; # 551, 541의 열이 모두 추가


-- 상관서브쿼리 
-- 서로 다른 테이블의 데이터를 서로 비교하는 서브쿼리
select * from sample551;
select * from sample552;
# sample522를 조회해서 sample552에 있는 no 값만 sample551에 업데이트하고 싶다면?

update sample551 set a = 1 where exists (select * from sample552 where no2 = no);
select * from sample551;

update sample551 set a = 0 where not exists (select * from sample552 where sample552.no2 = sample551.no);
select * from sample551;

use sample;

select * from sample551 where no = 1 or no = 2 or no = 5;
select * from sample551 where no in (1, 2, 5); # 열과 열을 비교


