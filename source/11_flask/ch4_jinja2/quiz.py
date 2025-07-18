from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        numb=None
    elif request.method == 'POST':
        try :
            numb = int(request.form.get('numb')) # POST 방식으로 넘어온 numb
        except :
            numb = 2
    return render_template('quiz.html', numb=numb)

# @app.route('/', methods=['GET', 'POST'])
# def index(numb=None):
#     if request.method == 'POST':
#         numb = request.form.get('numb') # POST 방식으로 넘어온 numb
#     return render_template('quiz.html', numb=numb)

if __name__ == '__main__':
    app.run(debug=True, port=8000)