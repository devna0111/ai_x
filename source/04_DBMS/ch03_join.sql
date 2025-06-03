-- [ III ] JOIN문 : 2개 이상의 테이블을 연결하여 데이터를 검색하는 방법
SELECT * FROM EMP WHERE ENAME = 'SCOTT'; --1행
SELECT * FROM DEPT; -- 4행
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
-- CROSS JOIN
SELECT *
    FROM EMP, DEPT 
    WHERE ENAME = 'SCOTT'; -- 1(EMP개수) * 4(DEPT개수) = 4개 행 반환
 --------------------------------------------------------------------------------------------------------------------  
 --------------------------------------------------------------------------------------------------------------------
-- ★1. EQUI JOIN(공통필드 값이 일치되는 조건만 JOIN)
SELECT EMP.ENAME, DEPT.DNAME, DEPT.LOC 
    FROM EMP, DEPT
    WHERE ENAME='SCOTT' AND EMP.DEPTNO = DEPT.DEPTNO;
    
SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, D.DEPTNO, DNAME, LOC 
    FROM EMP E, DEPT D -- 테이블에 ALIAS를 부여하면 지금부터 테이블은 ALIAS로만 접근이 가능하다
    WHERE ENAME='SCOTT' AND E.DEPTNO = D.DEPTNO;
    -- EX1. 모든 사원의 사번, 이름, 직책, 상사사번, 부서번호, 부서명, 근무지 출력
    SELECT EMPNO, ENAME, JOB, MGR, D.DEPTNO, DNAME, LOC 
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO;
    -- EX2. 급여가 2000이상인 사원의 이름, 직책,급여, 부서번호, 부서명, 근무지 출력
    SELECT ENAME, JOB,SAL, D.DEPTNO, DNAME, LOC 
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND SAL>=2000;
    -- EX3. 근무지가 CHICAGO인 직원의 이름, JOB, 급여, 부서번호
    SELECT E.ENAME, E.JOB, E.SAL, D.DEPTNO
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND D.LOC='CHICAGO';
    -- EX4. 82년도에 입사한 10,20번 부석 직원의 이름, 급여, 근무지(급여순)
    SELECT E.ENAME, E.SAL, D.LOC
        FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO 
                        AND TO_CHAR(E.HIREDATE,'YY') = '82' 
                        AND E.DEPTNO IN (10,20)
    ORDER BY SAL;
    -- EX5. JOB이 'SALESMAN'이거나 'MANAGER'인 사원의 이름, 급여, 상여, 연봉(SAL*12 + COMM), 부서명, 근무지를 연봉이 큰 순으로 출력
    SELECT E.ENAME, E.SAL, E.COMM, ((E.SAL+NVL(E.COMM,0))*12) AS "연봉", D.DNAME, D.LOC 
        FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND E.JOB IN ('SALESMAN','MANAGER')
    ORDER BY 연봉 DESC;
    -- EX6. COMM이 NULL이고 SAL이 2000대인 사원의 이름, 급여, 입사일, 부서번호, 부서명을 부서명 순, 급여순 정렬
    SELECT E.ENAME, E.SAL, E.HIREDATE, D.DEPTNO, D.DNAME
        FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND COMM IS NULL AND SAL LIKE '2___'
    ORDER BY D.DNAME, SAL;

    -- 탄탄1 뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오.
    SELECT E.ENAME, E.SAL
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND D.LOC = 'NEW YORK';
    -- 탄탄2 ACCOUNTING 부서 소속 사원의 이름과 입사일을 출력하시오.
    SELECT E.ENAME, E.HIREDATE
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND D.DNAME = 'ACCOUNTING';
    -- 탄탄3 직급이 MANAGER인 사원의 이름, 부서명을 출력하시오
    SELECT E.ENAME, D.DNAME
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND E.JOB = 'MANAGER';
    -- 탄탄4 COMM이 NULL이 아닌 사원의 이름, 급여, 부서코드, 근무지를 출력하시오
    SELECT E.ENAME, E.SAL, E.DEPTNO, D.LOC
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND COMM IS NOT NULL;
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------

-- ★2. NON-EQUI JOIN

SELECT * FROM EMP WHERE ENAME = 'SCOTT'; -- 직원정보
SELECT * FROM SALGRADE; -- 급여등급 정보
SELECT *  FROM EMP, SALGRADE WHERE SAL BETWEEN LOSAL AND HISAL AND ENAME = 'SCOTT';
    -- EX1. 모든 사원의 사번, 이름, JOB, 상사사번, 급여, 급여등급(**등급 형태로)
    SELECT EMPNO,ENAME,JOB,MGR,SAL,GRADE||'등급' AS "GRADE"
    FROM EMP, SALGRADE
    WHERE SAL BETWEEN LOSAL AND HISAL;

    -- 탄탄 1 COMM이 NULL이 아닌 사원의 이름, 급여, 등급, 부서번호, 부서이름, 근무지를 출력하시오
    SELECT E.ENAME, E.SAL, S.GRADE, D.DEPTNO, D.DNAME, D.LOC
    FROM EMP E, SALGRADE S, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL AND COMM IS NOT NULL;
    -- 탄탄 2 이름, 급여, 입사일, 급여등급
    SELECT E.ENAME, E.SAL, E.HIREDATE, S.GRADE
    FROM EMP E, SALGRADE S
    WHERE SAL BETWEEN LOSAL AND HISAL;
    -- 탄탄3 이름, 급여, 급여등급, 연봉, 부서명을 부서명순으로 정렬하여 출력. 부서가 같으면 연봉(SAL+COMM)*12
    SELECT E.ENAME, E.SAL, S.GRADE, (E.SAL+NVL(E.COMM,0)*12) 연봉, D.DNAME
    FROM EMP E, SALGRADE S, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL
    ORDER BY D.DNAME, 연봉;
    -- 탄탄4 이름 업무 급여 등급 부서코드 부서명 출력. 급여가 1000~3000사이, 부서명, 업무명, 급여 큰 순
    SELECT E.ENAME, E.JOB, E.SAL,S.GRADE, D.DEPTNO, D.DNAME
    FROM EMP E, SALGRADE S, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL AND SAL BETWEEN 1000 AND 3000
    ORDER BY D.DNAME,JOB, SAL DESC;
    -- 탄탄5 이름, 급여, 등급, 입사일, 근무지, 81년에 입사한 사람, 등급 큰 순
    SELECT E.ENAME, E.SAL, S.GRADE, E.HIREDATE, D.LOC
    FROM EMP E, SALGRADE S, DEPT D
    WHERE E.DEPTNO = D.DEPTNO AND TO_CHAR(HIREDATE,'YY')=81
    ORDER BY S.GRADE DESC;
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------

-- ★3. SELF JOIN

SELECT * FROM EMP WHERE ENAME='SMITH';
SELECT * FROM EMP WHERE EMPNO=7902;
SELECT E.ENAME, E.MGR, M.ENAME AS "MANAGER NAME" FROM EMP E, EMP M WHERE E.MGR = M.EMPNO(+);
    -- EX. 모든 사원의 사번, 이름, 상사의 사번, 상사이름
    SELECT E.EMPNO, E.ENAME, M.EMPNO 상사사번, M.ENAME 상사이름
    FROM EMP E, EMP M
    WHERE E.MGR = M.EMPNO;
    -- EX. SMITH의 상사는 JONES이다 포멧으로 출력
    SELECT E.ENAME || ' 의 상사는 ' || M.ENAME|| '이다'
    FROM EMP E, EMP M
    WHERE E.MGR = M.EMPNO;

-- 탄탄1 매니저가 KING인 사원들의 이름과 직급을 출력하시오
SELECT E.ENAME, E.JOB 
FROM EMP E, EMP M 
WHERE E.MGR = M.EMPNO AND M.ENAME='KING';

-- 탄탄1 서브쿼리 활용
SELECT ENAME, JOB
FROM EMP
WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME='KING');

-- 탄탄2 SCOTT과 동일한 부서번호에서 근무하는 사원의 이름을 출력하시오
SELECT E.ENAME 
FROM EMP E, EMP M 
WHERE E.DEPTNO = M.DEPTNO AND M.ENAME='SCOTT' AND E.ENAME != 'SCOTT';

-- 탄탄2 서브쿼리절을 활용
SELECT ENAME FROM EMP
WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME = 'SCOTT') AND ENAME != 'SCOTT';

-- 탄탄3 SCOTT과 동일한 근무지에서 근무하는 사원의 이름을 출력하시오
SELECT E.ENAME FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC = (
SELECT D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND E.ENAME = 'SCOTT') AND E.ENAME != 'SCOTT';

--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------

-- ★4. OUTER JOIN : SELF JOIN, EQUI JOIN 시 조건이 만족하지 않는 행까지 화면에 출력하는 JOIN
    -- 배제된 행을 결과에 포함 시킬경우 (+)기호를 정보가 부족한 필드명 뒤에 덧붙임
    -- (1) SELF JOIN에서의 OUTER JOIN
    SELECT W.EMPNO, W.ENAME, W.MGR, M.EMPNO, M.ENAME
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+);
    -- 말단 직원
    SELECT M.ENAME  -- W.EMPNO, W.ENAME, W.MGR, M.EMPNO 
        FROM EMP W, EMP M
        WHERE W.MGR(+) = M.EMPNO AND W.ENAME IS NULL; -- 정상 내용 아래 상사의 역할을 하지 않는 말단 직원들의 정보
        -- EX. 모든 사원에 대해 'SMITH의 상사는 FORD다' ... 'KING의 상사는 없다'
        SELECT E.ENAME || ' 의 상사는 ' || NVL(M.ENAME,'없')|| '다'
            FROM EMP E, EMP M
            WHERE E.MGR = M.EMPNO(+);

    -- (2) EQUI JOIN에서의 OUTER JOIN
    SELECT * FROM DEPT; -- 10,20,30,40
    SELECT DISTINCT DEPTNO FROM EMP; -- 10,20,30
    
    SELECT ENAME, D.DEPTNO, DNAME
        FROM EMP E, DEPT D
        WHERE E.DEPTNO(+) = D.DEPTNO; -- EMP에서는 DEPTNO가 40인 게 없어서 출력되지 않음
            
-- 탄탄1 ENAME의 매니져는 ENAME입니다 형태로 출력
SELECT E.ENAME||'의 매니져는'||NVL(M.ENAME,'無')||' 입니다' FROM EMP E, EMP M WHERE E.MGR = M.EMPNO(+);
-- 탄탄2 사원 테이블과 부서 테이블을 조인하여 사원 이름과 부서번호와 부서명을 출력. 부서 테이블의 40번 부서와 조인할 사원 테이블의 부서번호가 없지만 40번 부서의 부서 이름도 출력
SELECT E.ENAME, D.DEPTNO, D.DNAME FROM EMP E, DEPT D WHERE E.DEPTNO(+) = D.DEPTNO;