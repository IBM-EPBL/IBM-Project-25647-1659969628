from flask import Flask,jsonify;

app = Flask(__name__)

users = [
    {"name":"Ram", "email":"Ram@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"}
]


@app.route('/')
def index():
    return "Hello Welcome"

#GET method
@app.route('/users',methods=['GET'])
def get():
    return jsonify(users)

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    return jsonify(users[user_id])

#POST method
@app.route('/users',methods=['POST'])
def create():
    user = {"name":"Krishna","email":"krish123@gmail.com"}
    users.append(user)
    return jsonify({'Created':user})

#PUT method
@app.route('/users/<int:user_id>',methods=['PUT'])
def user_update(user_id):
    users[user_id]['email'] = 'bob34@gmail.com'
    return jsonify({'Updated':users})

#DELETE method
@app.route('/users/<int:user_id>',methods=['DELETE'])
def del_user(user_id):
    users.remove(users[user_id])
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)