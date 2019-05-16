from . import routes


@routes.route('/')
def index():
    return "Hello World"
