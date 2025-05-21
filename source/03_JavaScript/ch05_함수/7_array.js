/* array함수 : 가변인자함수(파이썬에서 튜플매개변수)
* 매개변수가 0개 : length가 0인 배열 생성 return
* 매개변수가 1개 : length가 매개변수만큼의 크기인 배열 생성 return
* 매개변수가 2개 이상 : 매개변수로 배열을 생성 return
*/
function array(){// arguments(매개변수 배열)
    let result = [];
    if(arguments.length==1 && typeof(arguments[0])=='number'){
        // result = arguments[0] 만큼의 크기인 배열
        for(let cnt = 1 ; cnt <= arguments[0];cnt++){
            result.push(null);
        }
    }else if(arguments.length>=2){
        // result = arguments의 내용물로 배열 
        // for(let idx=0;idx<arguments.length;idx++){ // forEach불가.
        //     result.push(arguments[idx]);
        // }
        for(i of arguments){ // forEach불가.
            result.push(i);
        }
    }else if(arguments.length==1 && typeof(arguments[0])!='number'){
        for(i of arguments){ // forEach불가.
            result.push(i);
        }
    };
    return result;
};
var arr1 = array();
var arr2 = array(3);
var arr3 = array(3, 4, 5);
var arr4 = array('3');
console.log(arr1);
console.log(arr2);
console.log(arr3);
console.log(arr4);