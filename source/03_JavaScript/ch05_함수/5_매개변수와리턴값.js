console.log(pow(5,3));
// 선언된 매개변수보다 많은 매개변수로 호출 => 선언할 때 사용한 매개변수 개수만큼만 읽고 나머지는 무시
console.log(pow(5,2,'12','12','12','12','12'));
// 선언된 매개변수보다 적은 매개변수로 호출
console.log(pow(5));
console.log(pow());
function pow(x, y){
    // x의 y승을 return
    console.log('함수 내의 x : '+ x , 'y : ' + y);
    let result = 1 ;
    for(let cnt=1;cnt<=y;cnt++){ // y = undefined라면 cnt<=y 가 false가 되면서 for문을 실행하지 않음
        result *= x;
    }
    return result ;
};
// function pow(x, y){
//     // x의 y승을 return
//     return x**y ; // 이 경우 매개변수가 부족하면 NaN을 반환해버림
// };
function pow(x, y){
    // x의 y승을 return
    console.log('함수 내의 x : '+ x , 'y : ' + y);
    let result = 1 ;
    for(let cnt=1;cnt<=y;cnt++){ // y = undefined라면 cnt<=y 가 false가 되면서 for문을 실행하지 않음
        result *= x;
    }
    // return result ; // 리턴이 없으면 undefined로 return
};