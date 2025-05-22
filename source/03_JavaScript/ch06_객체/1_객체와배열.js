/* 파이썬에서 객체(클래스) 만들기
class Person : 
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def __str__(self) :
        return 'print 하면 뿌릴 내용들'
    def method(self):
        *** 실행 명령어 ***
    def eat(self, food) :
        print(self.name,'이',food,'를 먹는다.')
person = Person('이름', 20)
print(person)
print(person.name, person.age)
person.eat(불고기)
*/
// 아래는 자바스크립트에서 객체 생성 하는 방식
const person = {'name':'홍길동', 'age' : 20};
console.log('person : ', person['name'],person['age']);
console.log('person : ',person.name, person.age);
const arr = ['홍길동',20]; // {'0' : '홍길동', '1' : 20}
console.log('arr : ',arr[0],arr[1]);