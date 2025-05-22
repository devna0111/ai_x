class Student{
    constructor(name, kor, mat, eng, sci){ // 파이썬의 __init__()
        this.name = name ;
        this.kor = kor ;
        this.mat = mat ;
        this.eng = eng ;
        this.sci = sci ;
    };
    getSum(){
        return this.kor + this.eng + this.mat + this.sci;
    };
    getAvg(){
        return this.getSum()/4
    };
    toString(){
        let output = '';
        for(let key in this){
            if(key!='toString' && key!= 'getSum' && key!='getAvg'){
                output += key + ' : ' + this[key] + ' ' ;
            }else if(key == 'getSum'){
                output += key.substring(3).toLowerCase() +' : '+ this[key]() + ' ';
            }else if(key == 'getAvg'){
                output += key.substring(3).toLowerCase() + ' : ' + this[key]() + '\n';
            }//if
        }; // for문
        return output;
    };//toString 끝
};
var hong = new Student('홍',100,100,99,100);
console.log(hong);
console.log(`${hong}`); // `${toString 결과 볼 객체명}` => 파이썬 f-string과 동일한 기능!
console.log(hong);