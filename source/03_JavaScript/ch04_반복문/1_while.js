// 파이썬에서는
// i, sum = 0, 0
// while i <= 100 :
//     sum += i
//     i += 1

/* 
i=0;sum=0;
while(i<=100){
    sum +=i;
    i++
    } => 조건을 보고 반복(0번 이상 반복)

    do{
    반복할 명령어들;
    }while(조건); => 반복을 하고 조건을 체크(1번 이상 반복)
*/

// 1초 동안 while문을 몇 번 실행했는 지 출력
var now = new Date();
var startTime = now.getTime();
// console.log(startTime);
// console.log(startTime+1000);
var cnt = 0 ;
while(new Date().getTime() < (startTime+1000)){
    cnt++; // cnt 1 증가
}
console.log('while문 반복 횟수 : ', cnt);
startTime2 = new Date().getTime();
cnt=0;
do{
    ++cnt;
}while(new Date().getTime() < (startTime2+1000));
console.log('do~while문 반복 횟수 : ', cnt);