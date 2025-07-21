from flask import Flask, render_template, request, redirect, url_for, abort, session
# redirect : 강제 예외 발생용 | session : 로그인/로그아웃 처리용
from models import TodoRequest

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test123'

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

@app.route('/')
def index():
    '''로그인 성공 로직(session에 로그인 정보 넣기) 후 /todos로 리다이렉트'''
    session['user_id'] = "hong"
    session['user_name'] = "홍길동"
    # return redirect("/todos") # /todos(GET) 요청 경로로
    return redirect(url_for('todos')) # todos 함수로 리다이렉트

@app.route('/todos') # 전체 목록 보기
def todos():
    '''todo_data를 리스트로 변환하여 랜더링'''
    ret = list(todo_data.values()) # todo_data => dict list
    order = request.args.get('order','asc') # 정렬 순서 : asc / desc
    if order == 'desc':
        ret = ret[::-1] # ret.reverse()
    next_id = max(todo_data.keys()) + 1 if len(todo_data) > 0 else 1
    return render_template('todo/todos.html', todo_data=ret, next_id=next_id, order=order)

@app.route('/logout')
def logout():
    ''' session 값 clear /todos 리다이렉트 '''
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for("todos"))

@app.route("/todos/<int:id>") # 목록 하나만 자세히 보기
def todo(id):
    ''' 해당 id의 todo_data를 html로 랜더링 '''
    todo = todo_data.get(id)
    if todo:
        return render_template('todo/todo.html', todo=todo)
    else:
        abort(404, description='해당 할일이 없습니다.')

@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route('/create', methods=['POST'])
def create():
    ''' 새로운 할일(request.form) 등록 '''
    # print(request.form.to_dict())
    todo = TodoRequest(**request.form.to_dict())
    todo_data[todo.id] = todo.model_dump() # todo 객체를 dict로 변환하여 todo_data에 추가
    return redirect(url_for('todos')) # /todos로 GET방식 리다이렉트

@app.route('/update/<int:id>', methods=['GET']) # 수정할 수 있는 페이지로 리다이렉트
def getupdate(id):
    return render_template('todo/update.html', todo=todo_data.get(id))

@app.route('/update/<int:id>/<string:title>/<string:is_done>', methods=['PUT']) # 수정할 수 있는 페이지로 리다이렉트
def update(id, title, is_done):
    todo = todo_data.get(id)
    if todo :
        todo['title'] = title
        todo['is_done'] = True if is_done == 'True' else False
        todo_data[id] = todo
        return f"{id}번 {title} 수정 완료"
    return abort(404, description='해당 할일이 없습니다.')

# @app.route('/delete/<int:id>', methods=['DELETE']) # 수정할 수 있는 페이지로 리다이렉트
# def delete(id):
#     todo = todo_data.get(id)
#     if todo :
#         del todo_data[id]
#         return f"{id}번 삭제 완료"
#     return abort(404, description='해당 할일이 없습니다.')

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    todo = todo_data.get(id)
    if todo:
        del todo_data[id]
        return f'{id}번 삭제 완료'
    return abort(404, description='해당 id의 할일이 없습니다.')

if __name__ == '__main__':
    app.run(debug=True)