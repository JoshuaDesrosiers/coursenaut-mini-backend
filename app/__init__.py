from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/health',methods=['GET'])
    def health_check():
        return {'status':'ok','message':'the server is live and healthy!'}
    return app