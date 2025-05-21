let funVar = function() {
    console.log('1.매개변수 없는 일반 함수 호출');
};
funVar();
funVar = () => {
    console.log('2.매개변수 없는 화살표 함수 호출');
};
funVar();
funVar = function(i){
    console.log('3.매개변수가 하나 있는 일반 함수 호출');
    console.log('매개변수 값 = ' + i);
}
funVar(10);
funVar = i => {
    console.log('4.매개변수가 하나 있는 화살표 함수 호출');
    console.log('매개변수 값 = ' + i);
}
funVar(10);
funVar = function(i) {
    console.log('5.매개변수가 하나의 한줄짜리 일반 함수 호출 ' + i);
}
funVar(10);
funVar = i => console.log('6.매개변수가 하나의 한줄짜리 화살표 함수 호출 ' + i);
funVar(10);
funVar = function(x){
    return x**x;
};
console.log('7. return문만 있는 일반 함수 호출 ' + funVar(10));
funVar = x => x**x; // lambda x : x**x 동일
console.log('8. return문만 있는 화살표 함수 호출 ' + funVar(10));
funVar = function(x, y){
    return x*10 + y;
};
funVar = (x,y) => x*10 + y ;
console.log('9. 매개변수가 2개짜리 return문장의  화살표 함수 호출 ' + funVar(5,3));

var arr = [10,'홍길동','신림동'];
arr.forEach((data, idx)=>console.log(idx +'번째 : ' + data)); // 기존 문법 arr.forEach(function(data, idx){실행구문})에서 function이 익명함수여서 화살표함수로 표현 가능
arr.forEach(data => console.log(data));