i = Number('');
console.log('i = ',i);//0
i = parseFloat('');//NaN
console.log('i = ',i,' 타입 : ',typeof(i));//NaN
f = 10/3;
console.log('f = ', f,); // 정수/정수 => 실수형으로 반환
a = 10/0; // 10/0.0000000000000000000000000000000000000001
console.log('a = ', a,' 타입 : ',typeof(a)); // 0으로 나누면 infinity 반환

console.log('i가 NaN인지 여부 : ', isNaN(i));
console.log('f가 NaN인지 여부 : ', isNaN(f));
console.log('a가 NaN인지 여부 : ', isNaN(a));

console.log('i가 finite인지 여부 : ', isFinite(i)); // NaN도 무한수네?
console.log('f가 finite인지 여부 : ', isFinite(f)); // 3.333333333333333335 반환으로 true
console.log('a가 finite인지 여부 : ', isFinite(a)); // 무한수여서 false

console.log(!a instanceof isFinite); // 무한수여서 false