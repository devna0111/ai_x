import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','210.121.189.12:1521/xe')

from models import TodoRequest
from typing import List # 타입 체크

def get_todos(order) -> List[dict]:
    cursor = conn.cursor()
    if order == 'asc':
        sql = 'SELECT * FROM TODO ORDER BY ID'
    else:
        sql = 'SELECT * FROM TODO ORDER BY ID DESC'
    cursor.execute(sql)
    result = cursor.fetchall() # 튜플리스트
    keys = ['id', 'title' , 'is_done']
    todos = [dict(zip(keys, row)) for row in result]
    cursor.close()
    return todos

def get_next_id() -> int:
    cursor = conn.cursor()
    sql = 'SELECT NVL(MAX(ID),0)+1 FROM TODO'
    cursor.execute(sql)
    result = cursor.fetchone() # 단일 튜플로 반환 -> (int,) 형태
    cursor.close()
    return result[0]

def get_todo(id:int) -> TodoRequest:
    cursor = conn.cursor()
    sql = 'SELECT * FROM TODO WHERE ID = :id'
    cursor.execute(sql, {'id' : id})
    result = cursor.fetchone() # (1, '바꿀내용', 0)
    cursor.close()
    return {'id' : result[0], 'title' : result[1], 'is_done' : result[2]}

def create_todo(todo:TodoRequest) -> int:
    cursor = conn.cursor()
    sql = 'INSERT INTO TODO (ID, CONTENTS, IS_DONE) VALUES (:id, :title, :is_done)'
    cursor.execute(sql, todo.model_dump())
    conn.commit()
    cursor.close()
    return cursor.rowcount # 추가 성공 시 1, 실패 시 0 리턴

def update_todo(todo:TodoRequest) -> int:
    cursor = conn.cursor()
    sql = 'UPDATE TODO SET CONTENTS = :title, IS_DONE = :is_done WHERE ID = :id'
    cursor.execute(sql, todo.model_dump())
    conn.commit()
    cursor.close()
    if cursor.rowcount == 1:
        return f"{todo.id}번 {todo.title} 수정 완료"
    else:
        return f"수정 실패"

def delete_todo(id:int) -> int:
    cursor = conn.cursor()
    sql = 'DELETE FROM TODO WHERE ID = :id'
    cursor.execute(sql, {'id' : id})
    conn.commit()
    cursor.close()
    if cursor.rowcount == 1:
        return f"{id}번 삭제 완료"
    else:
        return f"삭제 실패"

if __name__ == '__main__':
    # todos = get_todos('asc')
    # print("/todos :",todos)
    # print("next_id :",get_next_id())
    # print("/todos/1 :",get_todo(1))
    for _ in range(20) :
        test = TodoRequest(id=get_next_id(), title=f'flask_DB연동_체크{_}', is_done=False)
        print("/create :",create_todo(test))
    # test = TodoRequest(id=2, title='flask_DB연동_공부_공부', is_done=False)
    # print("/update :",update_todo(test))
    # print("/delete :",delete_todo(490))
