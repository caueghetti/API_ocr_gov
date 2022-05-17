from flask import Flask
from flask_restx import Api

import Configs

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(
                self.app,
                version='1.0.0',
                title='OCR GOV.BR API',
                description="OCR GOV.BR API",
                doc='/docs'
            )
    def run(self,):
        self.app.run(
            debug=False,
            host=Configs.get_ip(), 
            port=5002
        )

server = Server()