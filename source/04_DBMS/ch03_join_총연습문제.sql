--Part1
--1. 모든 사원에 대한 이름, 부서번호, 부서명을 출력하는 SELECT 문장을 작성하여라.
SELECT ENAME, D.DEPTNO, DNAME 
    FROM EMP E, DEPT D 
    WHERE E.DEPTNO=D.DEPTNO;

--2. NEW YORK에서 근무하고 있는 사원에 대하여 이름, 업무, 급여, 부서명을 출력
SELECT E.ENAME, E.JOB, E.SAL, D.DNAME  
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO AND D.LOC='NEW YORK';

--3. 보너스를 받는 사원에 대하여 이름,부서명,위치를 출력
SELECT E.ENAME, D.DNAME , D.LOC
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO AND E.COMM IS NOT NULL AND COMM > 0;
    
--4. 이름 중 L자가 있는 사원에 대하여 이름,업무,부서명,위치를 출력
SELECT E.ENAME, E.JOB, D.DNAME , D.LOC
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO AND E.ENAME LIKE '%L%';
    
--5. 사번, 사원명, 부서코드, 부서명을 검색하라(단, 사원명기준으로 오름차순 정렬)
SELECT E.EMPNO, E.ENAME,E.DEPTNO, D.DNAME
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO
    ORDER BY E.ENAME ASC;
    
--6. 사번, 사원명, 급여, 부서명을 검색하라. 
    --단 급여가 2000이상인 사원에 대하여 급여를 기준으로 내림차순으로 정렬하시오
SELECT E.EMPNO, E.ENAME,E.SAL, D.DNAME
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO AND SAL>=2000
    ORDER BY SAL DESC;
    
--7. 사번, 사원명, 업무, 급여, 부서명을 검색하시오. 단 업무가 MANAGER이며 급여가 2500이상인
-- 사원에 대하여 사번을 기준으로 오름차순으로 정렬하시오.
SELECT E.EMPNO, E.ENAME,E.JOB, E.SAL, D.DNAME
    FROM EMP E, DEPT D  
    WHERE E.DEPTNO=D.DEPTNO AND E.JOB = 'MANAGER' AND SAL>=2500
    ORDER BY E.EMPNO ASC;
    
--8. 사번, 사원명, 업무, 급여, 등급을 검색하시오(단, 급여기준 내림차순으로 정렬)
SELECT E.EMPNO, E.ENAME,E.JOB, E.SAL,S.GRADE
    FROM EMP E, SALGRADE S
    WHERE SAL BETWEEN LOSAL AND HISAL
    ORDER BY SAL DESC;
    
--Part2
--1. 이름, 직속상사명
SELECT E.ENAME, M.ENAME 직속상사명
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO;

--2. 이름, 급여, 업무, 직속상사명
SELECT E.ENAME,E.SAL,E.JOB, M.ENAME 직속상사명
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO;

--3. 이름, 급여, 업무, 직속상사명 . (상사가 없는 직원까지 전체 직원 다 출력.
    --상사가 없을 시 '없음'으로 출력)
SELECT E.ENAME,E.SAL,E.JOB, NVL(M.ENAME, '없음') 직속상사명
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO(+);

--4. 이름, 급여, 부서명, 직속상사명
SELECT E.ENAME,E.SAL,D.DNAME, M.ENAME
FROM EMP E, EMP M, DEPT D
WHERE E.DEPTNO = D.DEPTNO AND E.MGR = M.EMPNO(+);

--5. 상사가 없는 직원과 상사가 있는 직원 모두에 대해 이름, 급여, 부서코드, 부서명, 근무지, 직속상사명을 출력하시오(단, 직속상사가 없을 경우 직속상사명에는 ‘없음’으로 대신 출력하시오)
SELECT E.ENAME,E.SAL,E.DEPTNO,D.DNAME,D.LOC, NVL(M.ENAME, '없음') 직속상사명
FROM EMP E, EMP M, DEPT D
WHERE E.DEPTNO = D.DEPTNO AND E.MGR = M.EMPNO(+);

--6. 이름, 급여, 등급, 부서명, 직속상사명. 급여가 2000이상인 사람
SELECT E.ENAME, E.SAL, S.GRADE, D.DNAME, M.ENAME
FROM EMP E, EMP M, SALGRADE S, DEPT D
WHERE E.SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO AND E.MGR = M.EMPNO AND E.SAL>=2000;

--7. 이름, 급여, 등급, 부서명, 직속상사명, (직속상사가 없는 직원까지 전체직원 부서명 순 정렬)
SELECT E.ENAME, E.SAL, S.GRADE, D.DNAME, M.ENAME
FROM EMP E, EMP M, SALGRADE S, DEPT D
WHERE E.SAL BETWEEN LOSAL AND HISAL AND E.DEPTNO = D.DEPTNO AND E.MGR = M.EMPNO(+)
ORDER BY D.DNAME;

--8. 이름, 급여, 등급, 부서명, 연봉, 직속상사명. 연봉=(급여+comm)*12으로 계산
SELECT E.ENAME, E.SAL, S.GRADE, D.DNAME, (E.SAL+NVL(E.COMM,0))*12 AS "연봉", M.ENAME
FROM EMP E, SALGRADE S, DEPT D, EMP M
WHERE E.DEPTNO = D.DEPTNO AND E.SAL BETWEEN LOSAL AND HISAL AND E.MGR = M.EMPNO;

--9. 8번을 부서명 순 부서가 같으면 급여가 큰 순 정렬
SELECT E.ENAME, E.SAL, S.GRADE, D.DNAME, (E.SAL+NVL(E.COMM,0))*12 AS "연봉", M.ENAME
FROM EMP E, SALGRADE S, DEPT D, EMP M
WHERE E.DEPTNO = D.DEPTNO AND E.SAL BETWEEN LOSAL AND HISAL AND E.MGR = M.EMPNO
ORDER BY D.DNAME, SAL DESC;

--10. 사원테이블에서 사원명, 사원의 상사를 검색하시오(상사가 없는 직원까지 전체).
SELECT E.ENAME, M.ENAME 상사
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO(+);

--11. 사원명, 상사명, 상사의 상사명을 검색하시오(self join)
SELECT E.ENAME, M.ENAME 상사, S.ENAME "상사의 상사"
FROM EMP E, EMP M, EMP S
WHERE E.MGR = M.EMPNO AND M.MGR = S.EMPNO;

--12. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오(outer join)
SELECT E.ENAME, M.ENAME 상사, S.ENAME "상사의 상사"
FROM EMP E, EMP M, EMP S
WHERE E.MGR = M.EMPNO(+) AND M.MGR = S.EMPNO(+);