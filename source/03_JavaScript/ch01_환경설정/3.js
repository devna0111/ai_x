/* 변수 선언 시 var(전역변수), let(지역변수), const(상수) */
sum=0;
for(let i=1; i<=5;i++){
    sum+=i;//sum = sum + i; 1+2+3+4+5 ; i => 6
    console.log('i = ',i,'일때 누적 합은 ',sum);
}
console.log('for문 끝')

