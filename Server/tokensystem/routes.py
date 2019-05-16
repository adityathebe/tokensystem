from tokensystem import app
from tokensystem.models import User, Token

@app.route('/')
def home():
  return 'Hello World'