from flask import Flask
from sitegu.ext import site


def create_app():
    app = Flask(__name__)
    site.init_app(app) 
    return app
    
app = create_app()

if __name__ == '__main__':

    app.run(debug=True)
