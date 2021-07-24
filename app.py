from validators import list_name_template
from flask import Flask, render_template, request
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('base.db')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if bool(request.args):
            data = request.args
        else:
            data = request.form
        list_name = list_name_template(db=db.all(), request_args=data)
        return list_name

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
