from flask import request, jsonify, make_response
from tokensystem import app, bcrypt, db
from tokensystem.models import User, Token

@app.route('/')
def home():
  return 'Hello World'

@app.route('/user', methods=['GET'])
def user():
  all_users = User.query.all()
  response = [{ 'id': x.id, 'username': x.username} for x in all_users]
  return jsonify({ 'users': response })


@app.route('/register', methods=['POST'])
def register():
  username = request.form.get('username')
  email = request.form.get('email')
  password = request.form.get('password')
  hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

  # 1. Make sure we have all the required data 
  # 2. Make sure the data are valid data ( is email valid ? is password length valid ?)
  # 3. Make sure another user doesn't exist with the same credentials

  new_user = User(username=username, email=email, password=hashed_password)
  db.session.add(new_user)
  db.session.commit()

  return make_response(jsonify(success=True), 201)
