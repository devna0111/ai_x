# class Member :
#     def __init__(self, name, id, pw, addr) :
#         self.name = name
#         self.id = id
#         self.pw = pw
#         self.addr = addr

# pip install pydantic
from pydantic import BaseModel, Field
class Member(BaseModel) :
    '''Pydantic을 사용한 회원정보 모델'''
    name : str = Field(min_length=2, max_length=10, description="이름")
    id : int = Field(gt=0,lt=100, description="아이디")
    # gt = 0 : id > 0,ge=0 : id>=0, lt = 1000 : id < 1000, le = 1000 : id <= 1000
    pw : str
    addr : str = Field(default="서울")

if __name__ == "__main__" :
    member = Member(name="hong", id=123, pw="1234")
    print(member)