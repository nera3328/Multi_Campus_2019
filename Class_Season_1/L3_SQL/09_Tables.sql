use sample;
show tables;

-- 합집합
select* from sample71_a;
select *from sample71_b;

-- Union 정렬
select * from sample71_a union select * from sample71_b union select * from sample31;
select * from sample71_a union select * from sample71_a union select * from sample71_b union select * from sample71_b order by age;

select * from sample71_a union select * from sample71_a union select * b as num from sample71_b order by num;

-- sample71_a:1,2,3
-- sample71_b : 2,20,11
-- union : 1,2,3,10,11 (중복제거)
-- 만약에 1,2,3,2,10,11과같이 select * from smaple71_a union all seselect * form sample71_b

--  교집합 : INTERSECT
--  차집합: EXCEPT(or MINUS)

--  곱집합(교차결합)
select * from sample72_x;
select * from sample72_y;
select * from sample72_x,sample72_y;
-- Union vs 교차결합 
select * from sample72_x union select * from sample72_y;   #붙임

--  Inner join
create table item(
code char(4) not null,
name varchar(10),
price integer,
category varchar(10)
);

create table stock(
code char(4),
date date
);

insert into item values('1','shoes', 100,'s'), ('2','bag',200, 'b'),('3','phone',1000,'p');
select * from item;

insert into stock values('1','2019-06-12'),('2','2019-06-13'),('3','2019-06-14');
select * from stock;

select name, date from item inner join stock on item.code=stock.code;

insert into item values ('4','clock',1000,'c');
select * from item;

insert into stock values ('5','2019-06-15');
select * from stock;

select item.name, stock.date from item left join stock on item .code=stock.code;
select item.name, stock.date from item right join stock on item .code=stock.code;

-- 책(p.292~)
--  교차결합 : 상품*재고수alter
--  상품. 상품코드, 상품명, 메이커명, 가격alter
select * from 상품, 재고수;
select * from 상품, 재고수 , where 상품.상품코드 = 재고수.상품코드 and 상품.상품분류='식료품'

select 상품. 상품코드, 상품명, 메이커명, 가격 from 상품, 재고수 where 상품.상품코드= 재고수.상품코드 and 상품.상품분류= '식료품';
select * from 상품2;
select * from 상품3;
select * from 메이커;

select 상품코드, 상품명, 메이커, 메이커코드 from 상품2 inner join 메이커 on 
inner join and 재고수. 상품.상품분류