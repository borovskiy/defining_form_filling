from validators import list_name_template
from flask import Flask, request
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('base.db')


@app.route('/get_form', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.args:
            list_name = list_name_template(db=db.all(), request_args=request.args)
            return list_name
        return None


if __name__ == '__main__':
    app.run(debug=True)
