
# Models
# token_schema = TokenSchema(strict=True)
# tokens_schema = TokenSchema(many=True, strict=True)


# Register Routes
# app.register_blueprint(routes)

from tokensystem import app

if __name__ == '__main__':
  app.run(debug=True)
