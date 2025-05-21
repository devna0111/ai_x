function sumALL(){
    var result = 0 ;
    if(arguments.length==0){
        result = -999;
    }else{
        for(i of arguments){
            result += i
        }
    }
    return result
};
// var sum1 = sumALL(); // -999 (매개변수가 없으면 -999를 리턴)
// var sum2 = sumALL(1); // 1 (매개변수가 1개 이상이면 누적값리턴)
// var sum3 = sumALL(1, 2, 3, 4, 5); // 15
// console.log(sum1);
// console.log(sum2);
// console.log(sum3);