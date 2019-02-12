from flask import Flask
from config import dict_config
app = Flask(__name__)
app.config.from_pyfile(dict_config['config'])

if __name__ == '__main__':
    app.run()