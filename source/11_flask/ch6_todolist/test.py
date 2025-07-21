# pip isntall flask

todo_data = {
    1 : {'id' : 1,
        'title' : 'flask 공부',
        'is_done' : True,
    },
    2 : {'id' : 2,
        'title' : 'Django 공부',
        'is_done' : False,
    },
}

ret =list(todo_data.values()) # dict list
print('첫 실행 시 할일 :',ret)
next_id = max(todo_data.keys()) + 1 if len(todo_data) > 0 else 1
print('다음 실행 시 할일 id :',next_id)

todo_data[next_id] = {
    'id' : next_id,
    'title' : '아이디어 공부',
    'is_done' : False,
}

ret = list(todo_data.values())
# print('다음 실행 시 할일 :',ret)
for todo in ret :
    # print(todo)
    print(todo['id'],todo['title'],todo['is_done'])