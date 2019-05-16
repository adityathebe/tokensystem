from flask import jsonify, make_response
from . import routes

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']


@routes.route('/users', methods=['GET', 'POST'])
def users():
    return jsonify({'users': [user for user in usersList]})


@routes.route('/user/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({'username': usersList[id]})


@routes.route('/user/<string:name>', methods=['GET'])
def getUserByName(name):
    # Show some user information
    return "Some info"


@routes.route('/user/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({'message': 'New user added'})
