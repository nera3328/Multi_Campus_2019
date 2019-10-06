show databases;
select * from sample54;
select min(a) from sample54; -- min값을 계산 할 때에는 NULL값은 무시

#a의 최소값과 같은 것을 뽑아
select a from sample54 where a = (select min(a) from sample54);
#제일 작은 no 값의 것을 뽑아
select a from sample54 where no = (select min(no) from sample54);

# a > avg(a)일 때의 no를 뽑아줘
select no from sample54 where a > (select avg(a) from sample54);

select * from sample51;
select (select count(*) from sample51)as len_51, (select count(*) from sample54)as len_54;
select * from sample54;

select * from sample54;
# a값을 a의 최대값으로 업데이트 하기
update sample54 set a = (select min(price) from sample54);
select  max(a) from sample54;

select a from sample54 where a = (select price from sample34);
select * from (select * sample54 order by no desc ) sample541;
 
 -- sample54의 길이와 sample51의 길이를 sample541의 a,b 열에 각각 추가해보세요
 

 insert into sample541 values ((select count(*) from sample54), (Select count(*) from sample51));
 
 -- value 대신 select 이용해 insert 사용
 
 insert into sample541 values(1,2);
 insert into sample541 select 1,2;
 select * from sample542;
 
 -- 상관쿼리 : 서로 다른 테이블의 colum값을 비교 
select * from sample551;       # 열 2개인 지 확인.
alter table sample551 drop b;  #  b열이 있을 경우 삭제
insert into sample54 select * from sample551;  #54에 551을 삽입
insert into sample54 select * from sample541;	#54에 542을 삽입
insert into sample54 select no, quantity from sample51;		#54에 51의 quantity와 no가 같은 것을 삽입
insert into sample54 select * from sample551;  #551, 541의 열이 모두 추가

update sample551 set a= 1 where not exists (select * from sample552 where no2=no);
select * from sample551;

update sample551 set a= 0 where not exists (select * from sample552 where no2=no);
select * from sample551;

select * from sample551;
select * from sample552;

# sample552를 조회해서 sample552에있는 no값만 sample551에 업데이트하고 싶다면?
update sample551 set a =1 where exists (select * from sample552 where no2 =no);
select * from sample551;

show databases;
use sakila;
show tables;
select * from customer;
select * from customer_list; # customer_list에 check_element 열 추가한 다음   
							 # 두 테이블의 id를 비교-> customer에 있는 사람의 customer_list의 check열에
							 # check열에 1이라고 업데이트 해보세요

alter table customer_list insert into check_elemnt;


use sample;
# skila로  열을 비교하려면 아래와 같은 방법은 어색
select * from sample551 wehre no=1 or no=2 or no=5;  #X
select * from sample551 wehre no=1 ,2,5;             #x
#이처럼 비교 할 것을 모아두면 열이 된다. 그러니 이케 in을 써    in : =
select * from sample551 where no in (1,2,5);   # 열과 열을 비교
select * from sample551 where no in (select no2 from sample552);  #no=2
# not in : !=
select * from sample551 where no not in (select no2 from sample552);

-- index는 열! table 안 어떤 열을 쓸 건지 정해 만들어주면 쓸수있음 (table과는 독립적인 개체)
-- 인덱스 기준으로 쿼리를 날릴 수 있음
-- View: 가상table, 메모리 상 저장되지 않음. Select * from (select * from sample34)->셀렉트에 의해 호출된 테이블34이 앞의 from에 포함.
-- 		  select에 대한 결과. 대신 시간을 많이 잡아먹는다는 단점.
--  [명령어]      [객체]       [객체명]
--  create        table          T1         
--  drop          index          T2
--                 view
--  alter table로 테이블의 특정 열 속성을 바꾸고 싶다면 (modicfy-속성//change-이름)