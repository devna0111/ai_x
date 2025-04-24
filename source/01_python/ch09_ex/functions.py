# functions.py = fn1,fn2,fn3,fn4,fn5,fn9
from customer import Customer
def fn1_insert_customer_info():
    '사용자로 부터 name, phone, email, grade, etc를 입력받아 Customer 객체 반환'
    import re
    name = input('이름 : ')
#    name_pattern = r'([가-힣]{2,})|[a-zA-Z]{3,}'
    name_pattern = r'[가-힣]{2,}'
    while not re.search(name_pattern,name) :
        print('이름을 제대로 입력하세요(한글로 2글만 이상) : ')
        name = input('이름')
    phone = input('전화 : ')
    email = input('메일 : ')
    while True :
        try :
            age = int(input('나이 : '))
            if not (0<age<130) :
                raise Exception
            break
        except :
            print('올바른 나이를 입력하세요.나이의 허용 범위는 1살 이상 130살 미만입니다..')
    try :
        grade = int(input('등급(1~5) : '))
        if grade < 1 :
            grade = 1
        if grade > 5 :
            grade = 5
    except :
        print('유효하지 않은 등급 입력시 1등급으로 초기화')
        grade = 1
    etc = input('기타 정보 : ')
    customer = Customer(name,phone,email,age,grade,etc)
    return customer

def fn2_print_customers(customer_list):
    '''
    저장된 정보를 양식에 맞춰 모두 불러옵니다.
    '''
    print('=' * 80)
    print(f'{"고객정보":^80}')
    print('-' * 80)
    print(f"{'GRADE':^5}\t{'이름':^3}\t{'전화':^13}\t{'메일':^20}\t{'나이':^3}\t{'기타'}")
    print('=' * 80)
    for customer in customer_list :
        print(customer)
    print('=' * 80)

# 본인 풀이 : 원하는 정보/해당하는 정보를 선택하여 삭제하기

def fn3_delete_customer(customer_list):
    '''
    삭제할 정보 보여주고 선택하게 하기
    '''
    name = input('삭제하실 이름을 입력하세요 : ')
    name_candidate = [customer.name for customer in customer_list]
    if not name in name_candidate :
        print('해당이름으로 가입된 정보가 없습니다.')
    else :
        name_list = []
        for idx, customer in enumerate(customer_list) :
            if customer.name == name :
                name_list.append(customer_list[idx])
        print('확인된 정보는 아래와 같습니다.')
        print('=' * 80)
        print(f'{"고객정보":^80}')
        print('-' * 80)
        print(f"{'GRADE':^5}\t{'이름':^3}\t{'전화':^13}\t{'메일':^20}\t{'나이':^3}\t{'기타'}")
        print('=' * 80)
        for idx, customer in enumerate(name_list) :
            print(idx+1, customer)
        print('=' * 80)
        try :
            while True :
                numb = int(input('삭제하고자 하는 정보는 몇 번째 정보입니까?(취소 : 취소입력) : '))
                if (numb-1) in range(len(name_list)) :
                    break
                else :
                    print('올바른 순번을 입력하세요.')
            name_list.pop(numb-1)
            print(f'{name}님의 {numb}번째 정보를 삭제하였습니다.')
            for data in customer_list :
                if data.name == name and data not in name_list :
                    customer_list.remove(data)
        except :
            print('정보를 확인해주세요')

def fn4_search_customer(customer_list):
    '''
    입력받은 이름 정보를 모두 출력
    '''
    find_name = input('찾고자 하는 성함을 입력하세요 : ')
    name_list = []
    for idx, customer in enumerate(customer_list) :
        if customer.name == find_name :
            name_list.append(customer_list[idx])
    if not name_list :
        print('찾고자 하는 정보가 없습니다.')
    else :
        print(f'{find_name}님의 이름으로 입력된 정보는 아래와 같습니다..')
        fn2_print_customers(name_list)

def fn5_save_customer_csv(customer_list):
    '''
    매개변수로 받은 customer_list를 딕셔너리 리스트로 변환
    '''
    import csv
    try :
        file_name = input('저장할 파일 이름을 입력하세요')
        csv_list = [customer.as_dic() for customer in customer_list]
        with open(f'data/{file_name}.csv', 'w', encoding='utf-8', newline='') as f :
            writer = csv.DictWriter(f, fieldnames=csv_list[0].keys())
            writer.writeheader()
            writer.writerows(csv_list)
        print(f'{file_name}.csv 파일 저장 완료입니다.')
    except IndexError:
        print('지정된 정보가 없습니다. 정보 내보내기가 불가합니다.')
    except Exception :
        print('잘못된 접근입니다.')

def fn9_save_customer_txt(customer_list):
    '''
    종료 하기 전에 customer_list를 txt에 저장하고 종료
    '''
    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f :
        for line in [customer.to_list_style() for customer in customer_list] :
            f.write(line)
            f.write('\n')
    print('백업하였습니다.')