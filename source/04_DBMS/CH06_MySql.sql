-- DCL(계정 생성, 권한 부여, 권한 박탈, 계정 삭제, 트랜잭션 명령어)
-- DDL(테이블 생성, 테이블 삭제, 제약조건, 시퀀스 없음, 타입)
-- DML(INSERT, UPDATE, DELETE는 ORACLE과 동일, SELECT에서 OUTER JOIN이 다름)
	-- OUTER JOIN, AND연산자 &&, OR = ||, 오라클 연결연산자 || 대신 CONCAT함수를 이용하여 연결연산자 대치
    
    SHOW databases; -- DATABASE들 리스트
    -- 데이터 베이스로 들어감
    USE WORLD;
    SHOW TABLES; -- DATABASE 내 테이블들
    SELECT * FROM CITY;
    DESC CITY;
    
    -- ---------------------------------
    -- -----------** DCL **-------------
    -- ---------------------------------
    
    CREATE USER USER01 IDENTIFIED BY 'PASSWORD'; -- 계정 생성
    GRANT ALL PRIVILEGES ON *.* TO USER01; -- DBA 권한 부여
    REVOKE ALL privileges ON *.* FROM USER01; -- 권한 박탈 (빨간 X창은 USER01의 형태를 정확하게 명시하지 않아서 발생)
    DROP USER USER01; -- 계정 삭제
    
    -- ---------------------------------
    -- -----------** DDL **-------------
    -- ---------------------------------
    /* MYSQL 타입 : NUMERIC(N, D), VARCHAR(N자리수), DATE => 가변시리즈
    정수 : TINYINT(1BYTE) => -127 ~ 127까지, SMALLINT(2BYTE), MEDIUMINT(3BYTE), INT/INTEGER(4BYTE), BIGINT(8BYTE)
    실수 : FLOAT(M, D) - 4BYTE, DOUBLE(M,D) - 8BYTE
    문자 : CHAR(자리수), TEXT(), MEDIUMTEXT(16MB), LONGTEXT(4GB)
    날짜 : DATE, DATETIME, TIME, YEAR, TIMESTAMP... 등
    */
    
    -- DDL이나 DML명령어는 데이터베이스 내에서 실행.
    SHOW databases; -- DB 리스트 확인
    create database DEVDB; -- DB 생성
    USE DEVDB; -- DB 접근(특정 데이터 베이스로 들어가는 명령어)
    SELECT DATABASE(); -- 현재 접근 중인 DB
    DROP TABLE EMP;
    DROP TABLE IF EXISTS EMP; -- EMP 테이블이 존재할 경우 제거하라;
    CREATE TABLE EMP(
		EMPNO NUMERIC(5) NOT NULL,
			PRIMARY KEY(EMPNO),
		ENAME VARCHAR(6) NOT NULL,
        NICKNAME VARCHAR(6) UNIQUE,
        SAL NUMERIC(7,2) CHECK(SAL >0),
        COMM NUMERIC(7,2) DEFAULT 0
        );
DESC EMP;
insert into emp (empno, ename, nickname, sal) values (1,'홍길동길동동', '길다길다길어',-1); -- check 조건 위배로 에러
insert into emp (empno, ename, nickname, sal) values (1,'홍길동길동동', '길다길다길어',1000);
select * from emp;

-- 시퀀스 대체
-- MySql에서 100, 110, 120, ... 을 인위적인 primary key 사용
use devdb;
set @@auto_increment_increment = 1; -- 기본값 1, 증가값 설정 가능
set @@auto_increment_offset = 1; -- 기본값 1, offset은 최대 increment값 까지 가능
drop table if exists major;
create table major(
	mcode int primary key auto_increment,
    mname varchar(30),
    moffice varchar(30)
    );
desc major;
insert into major (mname, moffice) values ('컴공', 'm102호'); -- auto_increment 필드는 값을 대입하면 안되므로 필드값을 반드시 설정해줘야함..
insert into major (mname, moffice) values ('AI', 'm103호');
insert into major values (7,'빅데이터', 'm104호'); -- 작동은 함 그러나 다음 auto_increment가 7부터 시작하게 변경됨. 의미가 없어짐.
insert into major (mname, moffice) values ('컴싸', 'm104호');
select * from major;

drop table if exists student;
create table student(
	sno numeric(4) primary key,
    sname varchar(30) not null,
    mcode int references major(mcode)
		-- ,foreign key(mcode) references major(mcode)
	);

insert into student values(101,'홍길동',1);
insert into student values(102,'신길동',2);
insert into student values(103,'김길동',3);
insert into student values(104,'유길동',4);
desc student;
select * from student;

-- 오라클 (+)처럼 outer join 작동 안함
-- 이 경우 left join, right join, outer join을 활용
select * 
	from student s
    left outer join major m
    on s.mcode = m.mcode; 

drop table if exists student;
create table student(
	sno numeric(4) primary key,
    sname varchar(30) not null,
    mcode int
	,foreign key(mcode) references major(mcode)
	);
-- major mcode는 1,2,3. FK 조건에 의거 다른 mcode는 에러 발생
insert into student values(101,'홍길동',1);
insert into student values(102,'신길동',2);
insert into student values(103,'김길동',3);
insert into student values(104,'유길동',4); -- FK 조건에 의거 에러 발생
desc student;
select * from student;

select sno, sname, s.mcode, concat(mname,'학과'), moffice
	from student s, major m
    where s.mcode = m.mcode; -- 3번 학과는 출력되지 않음 : student에 3번 학과 소속이 없음
    
select sno, sname, s.mcode, concat(mname,'학과'), moffice
	from student s
    right outer join major m -- major가 3번 학과가 더 많음
    on s.mcode = m.mcode; -- 3번 학과는 출력되지 않음 : student에 3번 학과 소속이 없음

    -- ---------------------------------
    -- -----------** DML **-------------
    -- ---------------------------------
drop table if exists division;
create table division(
	DNO int not null primary key,
    dname varchar(20),
    phone varchar(20),
    position varchar(20));
show tables; -- 현 DB 내의 테이블 리스트

drop table if exists personal;
create table personal (
	pno int primary key,
	pname varchar(10) not null,
    job varchar(15) not null,
    manager int,
    startdate date,
    pay int, 
    bonus int,
    dno int ,
    foreign key(dno) references division(dno));
show tables;

desc division;
insert into division values (10, 'finance','02-777-7777','종로');
insert into division values (20, 'research','041-888-7777','대전');
insert into division values (30, 'sales','02-999-7777','인천');
insert into division values (40, 'marketing','02-555-7777','강남');

insert into personal values (1111,'smith','manager', 1001, '1990-12-17', 1000, null, 10);
insert into personal values (1112,'ally','salesman',1116,'1991-02-20',1600,500,30);
insert into personal values (1113,'word','salesman',1116,'1992-02-24',1450,300,30);
insert into personal values (1114,'james','manager',1001,'1990-04-12',3975,null,20);
insert into personal values (1001,'bill','president',null,'1989-01-10',7000,null,10);
insert into personal values (1116,'johnson','manager',1001,'1991-05-01',3550,null,30);
insert into personal values (1118,'martin','analyst',1111,'1991-09-09',3450,null,10);
insert into personal values (1121,'kim','clerk',1114,'1990-12-08',4000,null,20);
insert into personal values (1123,'lee','salesman',1116,'1991-09-23',1200,0,30);
insert into personal values (1226,'park','analyst',1111,'1990-01-03',2500,null,10);

select * from division;
select * from personal;

-- ----------------------------
-- ----------연습문제----------
-- ----------------------------
use devdb;
desc personal; -- pno(사번), pname(사원명), job(직책,일), manager(상사사번), startdate(고용일), pay(급여), bonus(상여), dno(소속부서번호)
desc division; -- dno(부서번호), dname(부서명), phone(대표번호), position(위치)
-- 1. 사번, 이름, 급여를 출력
select pno, pname,pay from personal;
-- 2. 급여가 2000~5000 사이 모든 직원의 모든 필드
select * from personal where pay between 2000 and 5000;
-- 3. 부서번호가 10또는 20인 사원의 사번, 이름, 부서번호
select pno, pname, dno from personal where dno in (10,20);
-- 4. 보너스가 null인 사원의 사번, 이름, 급여 급여 큰 순정렬
select pno, pname, pay from personal where bonus is null order by pay desc;
-- 5. 사번, 이름, 부서번호, 급여. 부서코드 순 정렬 같으면 PAY 큰순
select pno, pname, dno, pay from personal order by dno, pay desc;
-- 6. 사번, 이름, 부서명
select pno, pname, dname from personal p, division d where p.dno = d.dno;
-- 7. 사번, 이름, 상사이름
select p.pno, p.pname, m.pname managername from personal p, personal m where p.manager = m.pno;
-- 8. 사번, 이름, 상사이름(상사가 없는 사람도 출력하되 상사가 없는 경우 ★CEO★로 출력) 
select p.pno, p.pname, ifnull(m.pname,'★CEO★') managername from personal p left outer join personal m on p.manager = m.pno;
-- 8-1 사번, 이름, 상사사번(상사가 없으면 ceo로 출력. ifnull함수의 매개변수의 타입이 상이해도 상관없음)
select p.pno, p.pname, ifnull(m.pno,'CEO') managername from personal p left outer join personal m on p.manager = m.pno;
-- 8-2. 사번, 이름, 상사이름, 부서명(상사가 없는 사람도 출력) – 같이 합시다
select w.pno, w.pname, m.pname 상사명, d.dname 
from division d, personal w left outer join personal m on w.manager = m.pno 
where d.dno=w.dno;
select p.pno, p.pname, m.pname 상사명, d.dname from personal p left outer join personal m on p.manager = m.pno left outer join division d on p.dno = d.dno;
select p.pno, p.pname, m.pname 상사명, d.dname 
	from personal p 
    left outer join personal m 
    on p.manager = m.pno 
    left join division d 
    on p.dno = d.dno;
-- 9. 이름이 s로 시작하는 사원 이름 (like 이용)
select pname from personal where pname like 's%';
-- 10. 사번, 이름, 급여, 부서명, 상사이름
select p.pno, p.pname, p.pay, d.dname, m.pname 상사명 from personal p, personal m, division d where p.manager = m.pno and p.dno = d.dno;


-- Oracle과 다른 함수들
select pnaem||'님'||job from personal; -- || : OR 연산자
select concat(pname,'님은 ',job) from personal;

select sysdate(); -- 괄호만 추가
-- date_format(날짜/시간데이터, format)  => to_char(hiredate, 'yy/mm/dd') : 날짜형을 문자로
-- date_format(문자,                  format) => 문자형을 날짜형으로
	-- format : %Y 연도 네자리, %y 연도 두자리, %m 월별 (01,02,03,...12), %c 월별 (1,2,3,...12)
    -- %d(01,02,03,...31) 일별 %e(1,2,3,....30,31) 일별 %H 24시간 %h 12시간 %p 오전,오후 %i 분 %s 초
select date_format(sysdate(), '%y/%m/%d %H:%i:%s' ) 시간;

-- 오라클의 nvl() 대신 if()함수나 ifnull( )함수 사용 
select pno, pname, job, if(manager is null, 'CEO', manager) manager, startdate, pay, ifnull(bonus, 0) bonus, dno  from personal;
select pno, pname, job, if(manager is null, 'CEO', manager) manager, startdate,pay, if(pay>=3000, '부자','평범') 계급, ifnull(bonus, 0) bonus, dno  from personal;