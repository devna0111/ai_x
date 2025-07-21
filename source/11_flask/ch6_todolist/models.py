# pip install pydantic
from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    id : int
    title : str
    is_done : bool | None=False

if __name__ == '__main__':
    todo = TodoRequest(id="1", title='flask 공부', is_done=True)
    # print(todo.dict()) # todo 객체를 dict로 변환
    # print(todo.__dict__) # todo 객체를 dict로 변환
    print(todo.model_dump()) # todo 객체를 dict로 변환
    todo = TodoRequest(id="2", title='Django 공부')
    print(todo.model_dump()) # todo 객체를 dict로 변환
