function pow(x=1, y=2){
    // x의 y승을 return
    return x**y ;
};
console.log(pow(3,3));
console.log(pow(5));
console.log(pow());
// function pow(x=1, y=2){
//     // x의 y승을 return
//     let result = 1 ;
//     for(let cnt=1;cnt<=y;cnt++){
//         result *= x;
//     }
//     return result ;
// };