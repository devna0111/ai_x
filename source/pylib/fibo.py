def fibonacci_print(n) :
    '''
    매개변수도 들어온 n값 미만의 피보나치 수열을 출력
    ex. n = 10이면 0, 1, 1, 2, 3, 5, 8 print
    '''
    a,b = 0, 1
    while a < n :
        print(a, end = ' ')
        a, b = b, a+b
    print() # 개행

def fibonacci_return(n) :
    '''
    매개변수도 들어온 n값 미만의 피보나치 수열을 리스트로 return
    ex. n = 10 이면 [0, 1, 1, 2, 3, 5, 8] return
    '''
    fibo = []
    a,b = 0, 1
    while a < n :
        fibo.append(a)
        a, b = b, a+b
    return fibo

def fibo(n) :
    '''
    매개변수 n번째 피보나치 수를 return
    '''
    answer = [0] * (n + 1)
    answer[0] = 0 ; answer[1] = 1
    for i in range(2, n+1) :
        answer[i] = answer[i-1] + answer[i - 2]
    return answer

'테스트 : python fibo.py / python fibo.py 200'

if __name__ == '__main__' :
    import sys
    print(sys.argv)
    if len(sys.argv) > 1 :
        n = int(sys.argv[1])
        print('1. print test : ', end='')
        fibonacci_print(n)
        print('2. return test :', fibonacci_return(n))
    else :
        print('1. print test : ', end='')
        fibonacci_print(100)
        print('2. return test :', fibonacci_return(100))