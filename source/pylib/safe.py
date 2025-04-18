def safe_index(lst, item) :
    '''
    리스트 속 item의 유무를 체크하고
    item이 있다면 item 요소의 인덱스를 반환하고
    없으면 -1을 반환
    lst : 나열 가능한데이터
    item : 찾을 데이터
    '''
#     if item in lst :
#         return lst.index(item)
#     else :
#         return -1
    return lst.index(item) if item in lst else -1