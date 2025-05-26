Date.prototype.getIntervalDay = function(otherday){
    // this와 otherday 사이의 날짜 수를 return
    return Math.trunc(Math.abs(this.valueOf() - otherday.valueOf())/(1000*60*60*24)); //Math.trunc() 소수점 버림 / round반올림 ceil올림 floor내림

    // return (this.getTime()-otherday.getTime()<0)?Math.trunc((otherday.getTime()-this.getTime())/(1000*60*60*24)):Math.trunc((this.getTime()-otherday.getTime())/(1000*60*60*24));

    // if(this.getTime() - otherday.getTime()<0){
    //     return Math.trunc((otherday.getTime()-this.getTime())/(1000*60*60*24))
    // }else{
    //     return Math.trunc((this.getTime()-otherday.getTime())/(1000*60*60*24))
    // }
};

