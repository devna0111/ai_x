from customer import Customer, load_customers, to_customer
from functions import fn1_insert_customer_info,fn2_print_customers,fn3_delete_customer, \
                      fn4_search_customer,fn5_save_customer_csv,fn9_save_customer_txt
from pathlib import Path

def main() :
    work_dir = Path(__file__).parent
    data_dir = work_dir / "data"
    if __name__ == "__main__":
        if not data_dir :
            data_dir.mkdir(exist_ok=False)

    global customer_list
    customer_list = load_customers()
    while True :
        try :
            print('1:입력|2:전체출력|3:삭제|4:이름찾기|5:내보내기(csv)|9:종료')
            numb = int(input('메뉴 선택 : '))
            if numb not in [1,2,3,4,5,9] :
                raise Exception
            if numb == 1 :
                customer = fn1_insert_customer_info()
                customer_list.append(customer)
            elif numb == 2 :
                fn2_print_customers(customer_list)
            elif numb == 3 :
                fn3_delete_customer(customer_list)
            elif numb == 4 :
                fn4_search_customer(customer_list)
            elif numb == 5 :
                fn5_save_customer_csv(customer_list)
            elif numb == 9 :
                fn9_save_customer_txt(customer_list)
                print('프로그램을 종료합니다.')
                break
        except :
            print('잘못된 접근입니다.')

if __name__ == '__main__' :
    main()