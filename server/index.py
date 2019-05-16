from flask import Flask, jsonify, make_response

app = Flask('aditya')

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']


@app.route('/users', methods=['GET', 'POST'])
def users():
    return jsonify({'users': [user for user in usersList]})


@app.route('/user/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({'username': usersList[id]})


@app.route('/user/<string:name>', methods=['GET'])
def getUserByName(name):
    # Show some user information
    return "Some info"


@app.route('/user/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({'message': 'New user added'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 404)


app.run()
