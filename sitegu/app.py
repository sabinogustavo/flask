from flask import Flask
from sitegu.ext import site
from sitegu.ext import config
from sitegu.ext import toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app) 
    return app
    
app = create_app()

if __name__ == '__main__':

    app.run(debug=True)
