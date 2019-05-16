from flask import Flask

app = Flask('aditya')

from Routes import *
app.register_blueprint(routes)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 404)


app.run()
