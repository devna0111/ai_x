# jinja2 template 문법
# 1. 변수 정의 {{variable명}} 또는 {{variable명|filter}} 사용
#   filter : ch3에서 진행한 mask_pw
#           # 기본 제공 필터 : lower, upper, title, capitalize, length, replace, striptags, trim, escape,
#           #                 int, float, list, string ...
# 2. 제어문
#  2-1. if 제어문 {% if 조건 %} A태그 {% elif %} B태그 {% else %} C태그 {% endif %}
#  2-2. for 제어문 
#       {% for 변수 in 리스트 %} 
#           loop.index 인덱스 : 1부터 순번, loop.index0 : 0부터 순번,
#           loop.first : 첫번째 라인인지 여부, loop.last : 마지막 라인인지 여부
#       {% endfor %}
# 3. 헤더나 풋터 include {% include '파일명.html' %}
# 4. 서브 태그 {% block 블럭명 %} 내용 {% endblock %}
# 5. 주석 {%comment%} 내용 {%endcomment%}

from flask import Flask, render_template, request # 파라미터 값 접근

app = Flask(__name__,
            template_folder='templates', # template_folder 설정
            static_folder='static', # static_folder => css, js, img, ... 설정
            )

@app.errorhandler(404) # 예외 처리 페이지와 로깅
def not_found(error):
    app.logger.error(error, "없는 페이지입니다") # print와 차이가 없어 보이지만 log만 뽑아서 체크가 가능하다
    return render_template('404.html'), 404

names_list = [] # POST 방식으로 넘어온 name들 append

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        name = None
        name_len=0
    else:
        name = request.form.get('name') # POST 방식으로 넘어온 name
        names_list.append(name.strip()) # POST 방식으로 넘어온 name들 append
        name_len = len(name) # POST 방식으로 넘어온 name들 길이 구하기
    price = 12000 # 가격
    return render_template('index.html',
                            name=name,
                            names_list=names_list,
                            name_len=name_len,
                            price=price)

if __name__ == '__main__':    
    app.run(debug=True, port=8000)