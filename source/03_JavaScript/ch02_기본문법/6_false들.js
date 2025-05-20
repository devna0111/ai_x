// false로 간주되는 값 : undefined, 0, NaN, '', null, false
// Boolean(값) : boolean으로 형변환 
// String(값) : String으로 형변환
// Number(값) : number로 형변환
var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(null));
console.log(Boolean(Number('a')));
console.log(Boolean(''));
console.log(Boolean(' '));// true : 빈 스트링으로 주소가 할당되기 때문에.
console.log(Boolean([])); 
// 파이썬에서 빈 자료구조는 False를 반환하지만 자바스크립트에서 빈 object(배열[],{'name':'홍길동'})은 true를 반환
console.log(Boolean({}));