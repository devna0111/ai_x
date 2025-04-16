# 함수 정의
def my_hello(cnt) :
    for i in range(cnt) :
        print('hello, Python')
        print('hello, World')

# print(__name__) # 다른 페이지에 import 하면 파일 이름이 프린트된다.
# 함수 테스트
if __name__ == '__main__' :
    my_hello(3)